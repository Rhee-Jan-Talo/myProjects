

from django.shortcuts import render, redirect, get_object_or_404
import base64
########################################
from django.views.generic import View
from django.views import generic
from .models import *
from .utils import Calendar
from django.utils.safestring import mark_safe
from .utils import Calendar
import datetime
from datetime import date
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta


########################################

#import MySQLdb
import mysql.connector
import re
import os
from twilio.rest import Client
import random

from django.contrib import messages

from django.core.mail import send_mail

from django.conf import settings
from django.core.mail import EmailMessage


import json

############FORMS############
from .forms import user_accForm
from .forms import user_accFormEmail
from .forms import user_accForm2
from .forms import *

########AUTH#########
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


#####IMGUR######

from pathlib import Path
import requests, json
import pyimgur
from imgurpython import ImgurClient


def login_page(request):
    if request.user.is_authenticated == True:
        if request.user.username =="admin":
            return redirect('admin_order_requests')
        else:
            return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password'] #before mag authenticate i check sa user_acc if naa ang username with password (isave nlng pud ang default password para dli na mag change pass sa django db)
            username, password, is_exists = check_if_user_exists(username, password)
            if is_exists == True:
                user = authenticate(request,username=username,password=password)
            else:
                messages.error(request, 'Invalid username or password or User does not exist ')
                return render( request,'login_page.html', {})
            if user is not None:
                if username == "admin":
                    messages.error(request, f'Invalid username or password or User does not exist ' )
                    return render( request,'login_page.html', {})
                else:
                    login(request,user)
                    messages.error(request, f'Login success, Hi {username}!')
                    return redirect('home')
            else:
                messages.error(request, 'Invalid username or password or User does not exist ')
                return render( request,'login_page.html', {})
        else:
            return render( request,'login_page.html', {})

def login_admin(request):
    username = request.POST['username']
    password = request.POST['password']
    context= {}
    is_admin_exists = check_is_admin_exists(username, password)
    if is_admin_exists == True:
        username = "admin"
        user = authenticate(request, username="admin", password="p4$$word")
    else:
        messages.error(request, f'Invalid username or password or User does not exist')
        return render(request,'login_page.html', context)
    if user is not None:
        login(request, user)
        if username == "admin":
            messages.error(request, f'Welcome back!, Hi {username}!')
            return redirect('admin_order_requests')
        else:
            messages.error(request, f'Only admins are allowed to Enter!')
            return render(request,'login_page.html', context)
    else:
        messages.error(request, 'Invalid username or password or User does not exist')
        return render(request,'login_page.html', context)





def logout_user(request):
    messages.error(request, "Your Account Has been logged out")
    messages.error(request, f"See you again {request.user.username}")
    logout(request)
    return redirect('login_page')

@login_required
def about_us(request):
    upload_imgur_image()
    data = fetch_data(f'select * from farm left join contact_info on farm.farm_id = contact_info.farm_id left join social_info on farm.farm_id = social_info.farm_id;')
    for ii in data:
        org_chart_imgur = ii['org_chart_imgur']
    context= {'data':data,'org_chart_imgur':org_chart_imgur}
    return render(request,'about_us.html',context)

@login_required
def home_admin(request):
    return render(request,'home_admin.html',{})

@login_required
def home(request): 
    check_announcement_date_remaning()
    data = fetch_data("select * from announcements where a_status = 1;")
    user_data = fetch_data(f'select full_name from user_acc where username = "{request.user.username}"; ')
    for datas in user_data:
        full_name = datas['full_name']
    context ={"data":data,'full_name':full_name}
    return render(request,'home.html', context)



def register_email(request):
    form = user_accFormEmail(request.POST or None)
    context = {'form': form}
    if request.method =="POST":
        if form.is_valid():
            
            email = str(form.cleaned_data.get('email_ad'))
            pass1 = str(form.cleaned_data.get('passw'))
            pass2 = str(form.cleaned_data.get('confirm_passw'))
            boo,err_mess = validate_data_email(email,pass1,pass2)
            if boo == False:
                messages.error(request, err_mess[0])
                messages.error(request, err_mess[1])
                return render(request,"register_email.html", context)
            else:
                form.save()
                #PAG GAMIT UG LAING DUMMY ACCOUNT FOR THIS
                #REFER TO THIS YT VID: https://www.youtube.com/watch?v=1BaLWYUO1k4
                code = str(random.randint(0,999999))
                email = EmailMessage(
                    'Account Verification',#subject
                    f'Enter this code to verify your account: {code}',#message
                    'jarheetalo@gmail.com',#from
                    [email],) #to
                email.fail_silenty=False
                email.send()

                return redirect("confirm_email",code)
        else:
            return render(request,"register_email.html", context)
    else:
        return render(request,"register_email.html", context)


def confirm_email(request,code):
    if request.method =="POST":
        if request.POST['code'] != code:
            messages.error(request, 'ERROR: Invalid Code!')
            return redirect("confirm_email", code)
        else:
            new_data = user_account.objects.last()
            user_id = new_data.id
            return redirect("final_registration",user_id)

    else:
        return render(request,"confirm_email.html", {})


def register_phone(request):
    boo = True
    err_mess = []
    if request.method =="POST":
        form = user_accForm(request.POST or None)
        if form.is_valid():
            exists = check_user_already_exists(request.POST['username'])
            if exists == True:

                messages.error(request, "Username Already Exists")
                return redirect('register_phone')
            else:
                #email = str(form.cleaned_data.get('email_ad'))
                phone = str(form.cleaned_data.get('phone_num'))
                pass1 = str(form.cleaned_data.get('passw'))
                pass2 = str(form.cleaned_data.get('confirm_passw'))
                boo,err_mess = validate_data_phone(phone,pass1,pass2)
                if boo == False:
                    messages.error(request, err_mess[0])
                    messages.error(request, err_mess[1])
                    return render(request,"register_phone.html", {})
                else:
                    form.save()
                    #FROM MY TWILIO ACCOUNT
                    account_sid = "AC64b6d23ab97b6adedd0fd11465fcd59c"
                    auth_token = "9974f805ffcde70bf0ebee6c7654f510"
                    client = Client(account_sid, auth_token)
                    code = str(random.randint(0,999999))
                    #message = client.messages('MM800f449d0399ed014aae2bcc0cc2f2ec').fetch()
                    message = client.messages.create(body=code,from_= "+12292972135",to="+639939580551")
                    print(message.body)
                    return redirect("confirm_phone", code)  
        else:
            return render(request,"register_phone.html", {})
    else:
        return render(request,"register_phone.html", {})


def confirm_phone(request,code):
    if request.method =="POST":
        if request.POST['code'] != code:
            messages.error(request, 'ERROR: Invalid Code!')

            return redirect("confirm_phone", code)
        else:
            new_data = user_account.objects.last()
            user_id = new_data.id
            return redirect("final_registration",user_id)
    else:
        return render(request,"confirm_phone.html", {})



def final_registration(request,user_id):
    new_data = user_account.objects.get(id = user_id)
    context = {"data": new_data}
    if request.method =="POST":
        form = user_accForm2(request.POST or None)
        form2 = addressForm(request.POST or None)
        if form.is_valid() and form2.is_valid():
            form2.save()
            
            boo = validate_email(form.cleaned_data.get('email_ad'))
            boo2 = validate_phone(form.cleaned_data.get('phone_num'))
            if boo == False:
                messages.error(request, 'INVALID Email Format must containt @ and end in .com')
                return render(request,"final_registration.html", context)
            elif boo2 == False:
                messages.error(request, 'INVALID Phone Format please use (+63)')
                return render(request,"final_registration.html", context)

            else:
                new_data.full_name = form.cleaned_data.get('full_name')
                new_data.adress = form.cleaned_data.get('adress')
                new_data.phone_num = form.cleaned_data.get('phone_num')
                new_data.comp = form.cleaned_data.get('comp')
                new_data.email_ad = form.cleaned_data.get('email_ad')
                new_data.is_authenticated = True
                new_data.save()         
                #register the new account
                user = User.objects.create_user(new_data.username, new_data.email_ad, new_data.passw)
                user.first_name = form.cleaned_data.get('full_name')
                user.save()
                save_user(new_data)
                save_address(user_id)
                messages.error(request, 'Your Account has been registered please log in')
                return redirect("home")

        else:
            messages.error(request, 'INCORRECT INPUTS')
            return render(request,"final_registration.html", context)
    else:
        return render(request,"final_registration.html", context)

@login_required
def tbc_admin(request):
    user_id = user_account.objects.get(username=request.user.username)
    #data = user_order_request.objects.filter(user_id = user_id.id).filter(is_admin_approved = False)
    data = fetch_data(f"select * from user_order_request inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where user_id = {user_id.id} and is_admin_approved != 1;")
    context = {"data": data, "user":user_id.id}
    return render(request,"tbc_admin.html", context)

@login_required
def tbc_user(request):

    user_id = user_account.objects.get(username=request.user.username)
    #data = user_order_request.objects.filter(user_id = user_id.id).filter(is_admin_approved = True)
    data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id =user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where user_order_request.user_id = {user_id.id} and user_order_confirmed.is_cancelled = 0 and user_order_confirmed.is_user_confirmed = 0;')
    context = {"data": data, "user":user_id}

    return render(request,"tbc_user.html", context)

@login_required
def sales_order(request,message):
    if message == "1":
        messages.error(request, 'Order has been confirmed')
    user_id = user_account.objects.get(username=request.user.username)
    #data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where is_user_confirmed = 1 and is_cancelled = 0 and user_order_request.user_id = {user_id.id};')
    data = fetch_data(f"select batch_harvest.batch_img_imgur, user_order_request.plant_name, delivery_info.delivery_status, user_order_confirmed.*,batch_harvest.batch_img from user_order_confirmed left join delivery_info on user_order_Confirmed.f_order_id = delivery_info.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where is_user_confirmed = 1 and is_cancelled = 0 and user_order_request.user_id = {user_id.id} and user_order_confirmed.is_received = 0")
    context={'data': data}
    return render(request,"sales_order.html", context)

@login_required
def success_orders(request):
    user_id = user_account.objects.get(username=request.user.username)
    data = fetch_data(f"select * from user_order_confirmed inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where is_user_confirmed = 1 and is_cancelled = 0 and user_order_request.user_id = {user_id.id} and user_order_confirmed.is_received = 1")
    context={'data': data}
    return render(request,"success_orders.html", context)

@login_required
def cancelled_orders(request):
    user_id = get_user_id(request.user.username)
    data = fetch_data(f"select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id =user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where is_cancelled = 1 and user_order_confirmed.u_order_id in (select u_order_id from user_order_request where user_id = {user_id})")
    context = {'data': data}
    return render(request,"cancelled_orders.html", context)

@login_required
def refund(request):
    user_id = get_user_id(request.user.username)
    data = fetch_data(f'select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where purchase_history.user_id = {user_id}')
    context = {'data': data}
    return render(request,"refund.html", context)  

@login_required
def redelivery(request):
    user_id = get_user_id(request.user.username)
    data = fetch_data(f'select * from re_delivery inner join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where purchase_history.user_id =  {user_id};')
    context = {'data':data}
    return render(request,"redelivery.html", context)  

 

@login_required
def browse_plants(request):
    query = f"select * from batch_harvest inner join plant_batch on batch_harvest.batch_id = plant_batch.batch_id inner join plant_profile on plant_batch.plant_id = plant_profile.plant_id where batch_harvest.batch_status = 'On Sale';"
    myresult = fetch_data(query)
    
    upload_to_imgur()
    context = {"data": myresult}
    set_quantity_to_inactive()
    return render(request,"browse_plants.html", context)     

@login_required
def plant_details(request,harvest_id):

    query = f"select * from batch_quantity_variations where batch_quantity_variations.harvest_id = {harvest_id} order by grade;"
    myresult = fetch_data(query)
    query2=f"select * from batch_harvest inner join plant_batch on batch_harvest.batch_id = plant_batch.batch_id inner join plant_profile on plant_batch.plant_id = plant_profile.plant_id where batch_harvest.harvest_id = {harvest_id};"
    plant_data = fetch_data(query2)
    for things in plant_data:
        batch_id = things['batch_id']
    plant_activities = fetch_data(f'select * from plant_monitoring where batch_id = {batch_id}')
    context = {"data": myresult, "plant_data": plant_data,'plant_activities':plant_activities}
    is_sold_out = set_to_sold_out(harvest_id)
    if is_sold_out == True:
        messages.error(request, "Sorry, This product is sold out")
        return redirect('browse_plants')
    return render(request,"plant_details.html", context)



@login_required
def tabular_form(request,t_type):
    user_id = get_user_id(request.user.username)
    if t_type == "tbc_admin":
        data = fetch_data(f"select * from user_order_request inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id inner join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id where user_id = {user_id} and is_admin_approved != 1;")
        
        context = {"data": data, "t_type":t_type,}
        return render(request,"tabular_form.html", context)

    elif t_type == "tbc_user":
        data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id =user_order_request.u_order_id where user_order_request.user_id = {user_id} and user_order_confirmed.is_cancelled = 0 and user_order_confirmed.is_received = 0 and is_user_confirmed = 0;')
        context = {
        "t_type":t_type, 'data': data
        }
        return render(request,"tabular_form.html", context)

    elif t_type == "cancelled_orders":
        data = fetch_data(f"select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id =user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id inner join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id and payment_methods.is_selected = 1 inner join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id where is_cancelled = 1 and user_order_confirmed.u_order_id in (select u_order_id from user_order_request where user_id = {user_id})")
        context = {"data": data, "t_type":t_type,}
        return render(request,"tabular_form.html", context)

    elif t_type == 'sales_order':
        data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id inner join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id and payment_methods.is_selected = 1 inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id where is_user_confirmed = 1 and is_received = 0 and is_cancelled = 0 and user_order_request.user_id = {user_id};')
        context = {"data": data, "t_type":t_type,}
        return render(request,"tabular_form.html", context)

    elif t_type == 'success_orders':
        data = fetch_data(f'select * from user_order_confirmed inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id inner join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id and payment_methods.is_selected = 1 left join purchase_history on delivery_info.transaction_id = purchase_history.transaction_id where user_order_request.user_id = {user_id} and is_received = 1')
        context = {"data": data, "t_type":t_type,}
        return render(request,"tabular_form.html", context)

    elif t_type == 'redelivery':
        data = fetch_data(f'select * from purchase_history inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id =user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join re_delivery on purchase_history.purchase_history_id = re_delivery.purchase_history_id where purchase_history.user_id = {user_id}')
        context = {"data": data, "t_type":t_type,}
        return render(request,"tabular_form.html", context)

    elif t_type == 'refund':
        data = fetch_data(f'select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id =user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where purchase_history.user_id = {user_id};')
        payment_methods = fetch_data(f'select * from payment_methods_for_refund inner join purchase_history on payment_methods_for_refund.purchase_history_id = purchase_history.purchase_history_id where purchase_history.user_id ={user_id}')
        context = {"data": data, "t_type":t_type, 'payment_methods':payment_methods}
        return render(request,"tabular_form.html", context)

    else:   
        context = {
        "t_type":t_type,
        }
        return render(request,"tabular_form.html", context)

@login_required
def purchase_plant(request, harvest_id):
 
    query = f"select * from batch_harvest inner join plant_batch on batch_harvest.batch_id = plant_batch.batch_id inner join plant_profile on plant_batch.plant_id = plant_profile.plant_id where batch_harvest.harvest_id = {harvest_id};"
    data = fetch_data(query)
    quantities = fetch_data(f"select * from batch_quantity_variations where batch_quantity_variations.harvest_id = {harvest_id} order by grade;")
    user_id = get_user_id(request.user.username)


    form = requestForm(request.POST or None)
    context = {"data": data, "quans" : quantities, "harvest_id":harvest_id,"form":form, "user_id": user_id}
    if request.method == "POST" and form.is_valid():
        form.save()
        new_data = user_order_request.objects.last()
        quan_id = int(json.loads(request.POST['grade'].replace("'", "\""))['quantity_id'])
        new_data.quantity_variations_id = int(quan_id)
        new_data.save()
        save_data(new_data)
        messages.error(request, 'Order request has been successfully sent')
        return redirect('tbc_admin')

    else:
        return render(request,"purchase_plant.html", context)
    
@login_required
def tbc_user_details(request, u_order_id):
    dp_due = cancel_if_not_paid(u_order_id)
    #data = fetch_data(f'select * from user_order_confirmed where u_order_id = {u_order_id}')
    data = fetch_data(f'select * from  user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_confirmed.harvest_id = batch_harvest.harvest_id where user_order_confirmed.u_order_id = {u_order_id};')
    for datas in data:
        f_order_id = datas['f_order_id']
        q_id = datas['quantity_variations_id']
        quan = datas['quantity'] #QUANTITY REQUESTED NOT QUANTITY CONFIRMED
    q_details = fetch_data(f'select * from batch_quantity_variations where quantity_id = {q_id}')
    q_data = {'units': 0, 'price_per_unit': 0, 'total_amount': 0,}
    for things in q_details:
        q_data['units'] = things['units']
        q_data['price_per_unit'] = things['price_per_unit']
        q_data['total_amount'] = float(things['price_per_unit']) * float(quan)

    payment_methods = fetch_data(f'select * from payment_methods where f_order_id = {f_order_id};')
    p_id = 0 
    for ii in payment_methods:
        p_id = ii['p_id']
    payments_done = fetch_data(f'select * from payments_done where p_id = {p_id}')
    paid = False
    for things in payment_methods:
        if things['is_selected'] == 1:
            paid = True

    refunds = fetch_data(f'select * from refund_details where f_order_id = {f_order_id};')
    
    context = {'dp_due':dp_due, 'payments_done':payments_done, 'data': data, 'refunds':refunds, 'q_data' : q_data,'payment_methods':payment_methods, 'paid':paid}
    
    if dp_due == True:
        messages.error(request, 'You failed to pay the Down Payment on time, the order will be automatically cancelled')
        return redirect('cancelled_orders')
    if request.method == "POST":
        reason = request.POST.get('reason')
        cancel_order(reason, f_order_id)
        messages.error(request, 'Order has been cancelled')
        return redirect('cancelled_orders')
    else:
        return render(request,"tbc_user_details.html", context)


@login_required
def payment(request, pmethod, p_id):
    data = fetch_data(f'select * from payment_methods inner join user_order_confirmed on payment_methods.f_order_id = user_order_confirmed.f_order_id where p_id = {p_id};')

    for things in data:
        u_order_id = things['u_order_id']
        dp = things['total_downpayment']
        fp = float(things['total_amount']) + float(things['delivery_fee'])
    context = {"pmethod" : pmethod, 'data': data,'dp':dp, 'fp':fp}
    if request.method =="POST":
        form = paymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            update_db_payment()
            messages.success(request, "Proof of payment has been saved")
            return redirect('tbc_user_details', u_order_id)
        else:
            context = {"pmethod" : pmethod, 'data': data, 'img':img, 'form':form}
            #messages.error(request, "ERROR")
            return render(request, "payment.html", context)
    else:
        return render(request, "payment.html", context)

def confirm_user(request, f_order_id):
    
    finalize_user_order(f_order_id)
    message= '1'
    return redirect('sales_order', message)

@login_required
def sales_order_details(request, f_order_id):
    data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id inner join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id and payment_methods.is_selected = 1 inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where user_order_confirmed.f_order_id = {f_order_id};')
    refunds = fetch_data(f'select * from refund_details where f_order_id = {f_order_id}')
    delivery_info = fetch_data(f'select * from delivery_info where f_order_id = {f_order_id}')

    payments_done = fetch_data(f'select * from payments_done inner join payment_methods on payments_done.p_id = payment_methods.p_id where payment_methods.f_order_id = {f_order_id} and is_selected = 1 ')
    context = {'delivery_info':delivery_info, 'data':data, 'refunds':refunds,'payments_done':payments_done}
    if request.method == 'POST':
        reason = request.POST.get('reason')
        cancel_order(reason, f_order_id)
        messages.error(request, "Order has been successfully cancelled")
        return redirect('cancelled_orders')
    else:
        return render(request, "sales_order_details.html", context)



@login_required
def delivery_info(request,f_order_id):
    data = fetch_data(f'select * from delivery_info inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where delivery_info.f_order_id = {f_order_id};')
    is_paid = fetch_data(f'select * from user_order_confirmed where f_order_id = {f_order_id} and fp_paid = 1;')
    context = {'data':data,'is_paid':is_paid}
    return render(request, "delivery_info.html", context)


@login_required
def tbc_admin_details(request,order_id):
    user_id = user_account.objects.get(username=request.user.username)
    data = fetch_data(f"select * from user_order_request inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id inner join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id where u_order_id = {order_id} and user_id = {user_id.id};")
    total=0
    for things in data:
        total = float(things["quantity"]) * float(things["price_per_unit"])
    context = {"data": data, "user":user_id, 'total':total}
    return render(request, 'tbc_admin_details.html', context)


@login_required
def success_orders_details(request,f_order_id):
    user_id = user_account.objects.get(username=request.user.username)
    userid = user_id.id
    is_refund = fetch_data(f'select * from user_order_confirmed inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join purchase_history on delivery_info.transaction_id = purchase_history.transaction_id inner join refund on purchase_history.purchase_history_id = refund.purchase_history_id where user_order_confirmed.f_order_id = {f_order_id}')
    is_redelivery = fetch_data(f'select * from user_order_confirmed inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join purchase_history on delivery_info.transaction_id = purchase_history.transaction_id inner join re_delivery on purchase_history.purchase_history_id = re_delivery.purchase_history_id where user_order_confirmed.f_order_id = {f_order_id}')
    data = fetch_data(f'select * from user_order_confirmed inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id inner join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id and payment_methods.is_selected = 1 where user_order_confirmed.f_order_id = {f_order_id}')
    try:
        data2 = fetch_data(f'select * from purchase_history inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id where delivery_info.f_order_id = {f_order_id}')
    except:
        data2 = None
    context={'data': data, 'data2': data2 , 'userid': userid,'is_redelivery':is_redelivery, 'is_refund':is_refund}
    form = historyForm(request.POST or None)
    if request.method == 'POST'and form.is_valid():
        form.save()
        p_history = purchase_history.objects.last()
        update_purchase_history(p_history)
        messages.error(request, 'Thank you for Submitting your Feedback!')
        return redirect('success_orders_details', f_order_id)
    else:
        return render(request,"success_orders_details.html", context)

@login_required
def cancelled_orders_details(request, f_order_id):

    data = fetch_data(f"select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where user_order_confirmed.f_order_id = {f_order_id};")
    #data = fetch_data(f"select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id inner join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id where user_order_confirmed.f_order_id = {f_order_id};")
    payment_methods = fetch_data(f'select * from payment_methods where f_order_id = {f_order_id} and is_selected = 1;')
    payment_done = fetch_data(f'select * from payments_done inner join payment_methods on payments_done.p_id = payment_methods.p_id where payment_methods.f_order_id = {f_order_id} and is_selected = 1;')
    delivery_info = fetch_data(f'select * from delivery_info where f_order_id = {f_order_id}')

    payment_methods_for_refund = fetch_data(f'select * from payment_methods_for_refund where f_order_id_for_refund = {f_order_id}')
    context = {'data': data,'delivery_info':delivery_info,'payment_done':payment_done,'payment_methods':payment_methods,'payment_methods_for_refund':payment_methods_for_refund}
    return render(request,"cancelled_orders_details.html", context)

@login_required
def refund_form(request, purchase_history_id):
    data = fetch_data(f'select * from purchase_history inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id =user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where purchase_history.purchase_history_id = {purchase_history_id}')
    payment_methods= fetch_data(f'select * from payment_methods_for_refund where purchase_history_id = {purchase_history_id}')
    form = refundForm(request.POST, request.FILES)
    quan_limit = get_quan_limit(data)
    context = {'data':data, 'payment_methods':payment_methods, 'quan_limit':quan_limit}
    if request.method == 'POST' and form.is_valid():
        if is_over(request.POST.get('refund_quan'),request.POST.get('quantity_received'),quan_limit) == True:
            messages.error(request,'There is a error in Quantity inputs please input the correct data')
            return redirect('refund_form', purchase_history_id)
        else:
            form.save()
            send_refund()
            update_pm_refund(purchase_history_id)
            messages.error(request, 'Refund Request has been submitted')
            return redirect('refund')

    else:
        return render(request,'refund_form.html',context)

def refund_details(request, refund_id):
    total_payment_done = 0
    data = fetch_data(f"select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id =user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where refund.refund_id = {refund_id}")
    payment_methods =fetch_data(f'select * from payment_methods_for_refund where refund_id = {refund_id}')
    for thingss in data:
        f_order_id = thingss['f_order_id']
    payment_methods1 = fetch_data(f'select * from payment_methods where f_order_id = {f_order_id} and is_selected = 1')
    for things in payment_methods1:
        total_payment_done = things['total_amount_paid']
    payment_methods_for_refund = fetch_data(f'select * from payment_methods_for_refund where refund_id = {refund_id}')
    context ={'total_payment_done':total_payment_done,'data':data,'payment_methods':payment_methods,'payment_methods_for_refund':payment_methods_for_refund}
    return render(request,'refund_details.html',context)


@login_required
def pm_refund(request, purchase_history_id):
    form = refundPMForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        form.save()
        pm_refund_save()
        messages.error(request, 'Payment Method has been added')
        return redirect('refund_form',purchase_history_id)
    context={'purchase_history_id':purchase_history_id}
    return render(request, 'pm_refund.html', context)

def pm_refund_order(request, f_order_id):
    form = refundPMForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        if request.POST['payment_method'].lower() in ['gcash', 'paymaya']:
            is_valid = validate_phone(request.POST['account_num'])
            if is_valid == False:
                messages.error(request, 'Invalid Account number, please double check')
                return redirect('pm_refund', f_order_id)
        form.save()
        pm_refund_save_order()
        messages.error(request, 'Payment Method has been added')
        return redirect('cancelled_orders_details',f_order_id)
    context={'f_order_id':f_order_id}
    return render(request, 'pm_refund.html', context)

@login_required
def redelivery_form(request, purchase_history_id):
    data = fetch_data(f'select * from purchase_history inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id =user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where purchase_history.purchase_history_id = {purchase_history_id}')
    #redelivery = fetch_data(f'select * from re_delivery where purchase_history_id = {purchase_history_id}')
    form =rdForm(request.POST, request.FILES)
    quan_limit = get_quan_limit(data)
    if form.is_valid():
        if is_over(request.POST.get('returned_quan'),request.POST.get('quan_received'),quan_limit) == True:
            messages.error(request,'There is a error in Quantity inputs please input the correct data')
            return redirect('redelivery_form', purchase_history_id)
        else:
            form.save()
            send_redelivery()
            messages.error(request, 'Request for Redelivery has been submitted')
            return redirect('redelivery')
    context = {'data':data,'redelivery':redelivery}

    return render(request, 'redelivery_form.html', context)

@login_required
def redelivery_info(request, rd_id):
    data = fetch_data(f'select * from redelivery_info where redelivery_info.re_delivery_id = {rd_id}')
    context= {'data':data}
    return render(request, "redelivery_info.html", context)

def redelivery_details(request, purchase_history_id):
    data = fetch_data(f'select * from purchase_history inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id =user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join re_delivery on purchase_history.purchase_history_id = re_delivery.purchase_history_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where purchase_history.purchase_history_id = {purchase_history_id}')
    
    context = {'data':data}
    return render(request,"redelivery_details.html", context) 



@login_required
def user_soa(request):
    user_id = get_user_id(request.user.username)
    data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where user_order_request.user_id = {user_id} order by user_order_request.u_order_id desc') # and is_cancelled != 1
    context = {'data': data}
    return render(request, 'user_soa.html', context)





@login_required
def user_deliveries(request):
    user_id = get_user_id(request.user.username)
    data = fetch_data(f'select * from delivery_info inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where user_order_request.user_id = {user_id}')
    context = {'data':data }
    return render(request,'user_deliveries.html', context)

@login_required
def user_refunds(request):
    user_id = get_user_id(request.user.username)
    data = fetch_data(f'select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id where purchase_history.user_id = {user_id}')
    context = {'data':data }
    return render(request,'user_refunds.html', context)

@login_required
def soa_billing(request, f_order_id):
    p_id = 0
    payment_method_selected = ""
    payment_method = fetch_data(f'select * from payment_methods where f_order_id = {f_order_id} and is_selected = 1')
    for things in payment_method:
        p_id = things['p_id']
        payment_method_selected = things['payment_method']
    data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where f_order_id = {f_order_id}')
    refund = fetch_data(f'select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id where user_order_confirmed.f_order_id = {f_order_id}')
    redelivery = fetch_data(f'select * from re_delivery inner join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id where user_order_confirmed.f_order_id = {f_order_id}')
    refund_id = 0
    for i in refund:
        refund_id = i['refund_id']
    payment_methods_for_refund = fetch_data(f'select * from payment_methods_for_refund where refund_id = {refund_id} and is_selected = 1;')
    payment_methods_for_cancel = fetch_data(f'select * from payment_methods_for_refund where f_order_id_for_refund ={f_order_id} and is_selected = 1;')
    payments_done = fetch_data(f'select * from payments_done where p_id = {p_id}')
    context = {'payment_methods_for_cancel':payment_methods_for_cancel,'payment_methods_for_refund':payment_methods_for_refund,'redelivery':redelivery,'refund':refund,'data':data, 'payment_method':payment_method,'payments_done':payments_done,'payment_method_selected':payment_method_selected}
    return render(request,'soa_billing.html', context)

@login_required
def profile(request):
    user_id = get_user_id(request.user.username)
    data = fetch_data(f'select * from user_acc inner join address on user_acc.user_id = address.user_id where user_acc.user_id = {user_id}')
    context = {'data':data }
    if request.method == 'POST':
        valid_email = validate_email(request.POST['email_ad'])
        valid_phone = validate_phone(request.POST['phone_num'])
        if valid_email and valid_phone == True:  
            update_profile_info(request)
            messages.error(request,'Profile Successfully Updated')
            return redirect('profile')
        elif valid_phone == False:
            messages.error(request,'Invalid Phone Number format')
            return redirect('profile')
        elif valid_email == False:
            messages.error(request,'Invalid Email format')
            return redirect('profile')
        else:
            messages.error(request,'Error occured, try again later')
            return redirect('profile')

    return render(request,'profile.html', context)

def edit_shipping_address(request):
    updpate_shipping_address(request)
    messages.error(request, 'Shipping Address Successfully Updated')
    return redirect('profile')

def change_password(request):
    data = fetch_data(f'select * from user_acc where user_id = {get_user_id(request.user.username)}')
    for i in data:
        og_pass = i['pass']
    context = {"data":data}
    if request.method == "POST":
        if og_pass == request.POST['old_pass']:
            if request.POST['new_pass'] == request.POST['conf_new_pass']:
                changepassword_db(request)
                logout(request)
                messages.error(request, 'Password successfully changed, you need to log in again')
                return redirect('login_page')
            else:
                messages.error(request, "Password does not match")
                return redirect('change_password')
        elif og_pass != request.POST['old_pass']:
            messages.error(request, 'Incorrect Old Password')
            return redirect('change_password')
        

    return render(request, 'change_password.html', context)

##########################ADMIN INPUTS##################################
@login_required
def admin_order_requests(request):
    query = f"select user_order_request.u_order_id, user_order_confirmed.is_received, user_order_confirmed.is_cancelled, user_order_request.plant_name, user_order_request.order_request_date,user_order_request.is_admin_approved, user_acc.full_name, user_order_confirmed.is_received, delivery_info.transaction_id as di_ready, payment_methods.p_id as pm_ready, count(payments_done.p_id) as cc from user_order_request left join user_order_confirmed on user_order_request.u_order_id = user_order_confirmed.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id left join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id left join (select * from payments_done where payments_done.is_confirmed = 0) as payments_done on payment_methods.p_id = payments_done.p_id where user_order_request.remove_to_view = 0 group by user_order_request.u_order_id desc"
    data  = fetch_data(query)
    context ={'data':data}
    if request.method == "POST":
        data = filter_order_requests(query, request.POST['submit'])
        context ={'data':data}
        return render(request, 'admin_order_requests.html', context)     
    return render(request, 'admin_order_requests.html', context)

@login_required
def admin_redelivery_requests(request):
    data = fetch_data("select * from re_delivery left join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id left join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id left join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select redelivery_info.re_delivery_id as rdo_ready,redelivery_info.re_delivery_status as rdi_ready from redelivery_info left join re_delivery on redelivery_info.re_delivery_id = re_delivery.re_delivery_id) as rd_ready on rd_ready.rdo_ready = re_delivery.re_delivery_id where re_delivery.remove_to_view = 0 order by re_delivery_id desc;")
    context = {'data': data }
    if request.method=="POST":
        data = filter_admin_redelivery(request.POST['submit'])
        context ={'data':data}
        return render(request, 'admin_redelivery_requests.html', context)

    return render(request, 'admin_redelivery_requests.html', context)

@login_required
def admin_refund_requests(request):
    data = fetch_data("select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.remove_to_view = 0 order by refund_id desc")
    context = {'data': data}
    if request.method == "POST":
        data = filter_admin_refund(request.POST['submit'])
        context = {'data': data}
        return render(request, 'admin_refund_requests.html', context)
    return render(request, 'admin_refund_requests.html', context)



@login_required
def admin_cancelled_orders(request):
    data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id  where is_cancelled = 1 and cancelled_remove_to_view = 0;')
    for things in data:
        if float(things['cancel_refund_amount']) <= 0:
            if things['refund_date'] == None or things['refund_date'] == "None" or str(things['refund_date']) == "":
                set_refund_paid(things['f_order_id'])
    context={'data':data}
    if request.method == "POST":
        data = filter_admin_cancelled(request.POST['submit'])
        context={'data':data}
        return render(request,'admin_cancelled_orders.html',context)
    return render(request,'admin_cancelled_orders.html',context)



def admin_cancelled_orders_details(request,f_order_id):
    data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where user_order_confirmed.f_order_id = {f_order_id}')
    payment_methods = fetch_data(f'select * from payment_methods_for_refund where f_order_id_for_refund = {f_order_id}')
    is_selected = False
    for ii in payment_methods:
        if ii['is_selected'] == 1:
            is_selected = True
    context={'data':data, 'payment_methods': payment_methods,'is_selected':is_selected}
    return render(request, 'admin_cancelled_orders_details.html', context)




@login_required
def admin_refund_action(request, refund_id):
    data = fetch_data(f'select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.refund_id = {refund_id}')
    payment_methods = fetch_data(f'select * from payment_methods_for_refund where refund_id = {refund_id}')
    context= {'refund_id':refund_id,'payment_methods':payment_methods, 'data': data}
    if request.method=="POST":
        accept_refund(refund_id)
        messages.error(request, 'Refund successfully accepted')
        return redirect('admin_refund_requests')
    else:
        return render(request, 'admin_refund_action.html', context)

def admin_refund_update(request, refund_id):
    data = fetch_data(f'select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.refund_id = {refund_id}')
    payment_methods = fetch_data(f'select * from payment_methods_for_refund where refund_id = {refund_id}')
    is_selected = fetch_data(f'select * from payment_methods_for_refund where refund_id = {refund_id} and is_selected = 1')

    context= {'refund_id':refund_id, 'data': data,'payment_methods':payment_methods,'is_selected':is_selected}
    return render(request, 'admin_refund_update.html', context)


def decline_refund(request,refund_id):
    reason = request.POST['decline_reason']
    decline_request_db(reason, refund_id)
    messages.error(request, 'Refund request successfully Declined')
    return redirect('admin_refund_requests')


def decline_redelivery(request,re_delivery_id):
    reason = request.POST['decline_reason']
    decline_redelivery_db(reason, re_delivery_id)
    messages.error(request, 'Redelivery request successfully Declined')
    return redirect('admin_redelivery_requests')


def admin_order_action(request, u_order_id):
    data = fetch_data(f"select * from user_order_request inner join batch_quantity_variations on user_order_request.quantity_variations_id =batch_quantity_variations.quantity_id inner join user_acc on user_order_request.user_id = user_acc.user_id where user_order_request.u_order_id = {u_order_id}")
    form = confirmForm(request.POST or None) 
    context ={'data':data, 'form': form}
    set_quantity_to_inactive()
    if request.method=="POST" and form.is_valid():
        form.save()
        save_confirm()
        send_email_order_confirmation(u_order_id)
        messages.error(request,"Order has been confirmed")
        return redirect('admin_order_requests')
    return render(request, 'admin_order_action.html',context)

def decline_order_request(request):
    decline_reason=request.POST['decline_reason']
    u_order_id=request.POST['u_order_id']
    decline_order(decline_reason, u_order_id)
    messages.error(request, f'Order No. {u_order_id} has been declined')
    return redirect('admin_order_requests')



def admin_order_update(request,u_order_id):
    data = fetch_data(f"select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id where user_order_request.u_order_id = {u_order_id}")
    delivery_info = fetch_data(f'select * from delivery_info inner join user_order_confirmed on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join user_order_request on user_order_request.u_order_id = user_order_confirmed.u_order_id where user_order_request.u_order_id = {u_order_id}')
    refund_details = fetch_data(f'select * from refund_details inner join user_order_confirmed on user_order_confirmed.f_order_id = refund_details.f_order_id inner join user_order_request on user_order_request.u_order_id = user_order_confirmed.u_order_id where user_order_request.u_order_id = {u_order_id} order by refund_details.date_from')
    payment_methods = fetch_data(f'select * from payment_methods inner join user_order_confirmed on user_order_confirmed.f_order_id = payment_methods.f_order_id inner join user_order_request on user_order_request.u_order_id = user_order_confirmed.u_order_id where user_order_request.u_order_id = {u_order_id}') 
    data_declined = fetch_data(f'select * from user_order_request inner join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id where u_order_id = {u_order_id}')
    is_paid = fetch_data(f'select * from user_order_confirmed where u_order_id = {u_order_id} and fp_paid = 1')
    context = {'is_paid': is_paid,'data_declined':data_declined,'u_order_id':u_order_id,'data': data, 'delivery_info': delivery_info, 'refund_details':refund_details, 'payment_methods':payment_methods}
    return render(request, 'admin_order_update.html', context)

def view_only_order_details(request,u_order_id):
    data = fetch_data(f"select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id inner join user_acc on user_order_request.user_id = user_acc.user_id where user_order_request.u_order_id = {u_order_id}")
    delivery_info = fetch_data(f'select * from delivery_info inner join user_order_confirmed on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join user_order_request on user_order_request.u_order_id = user_order_confirmed.u_order_id where user_order_request.u_order_id = {u_order_id}')
    refund_details = fetch_data(f'select * from refund_details inner join user_order_confirmed on user_order_confirmed.f_order_id = refund_details.f_order_id inner join user_order_request on user_order_request.u_order_id = user_order_confirmed.u_order_id where user_order_request.u_order_id = {u_order_id} order by refund_details.date_from')
    payment_methods = fetch_data(f'select * from payment_methods inner join user_order_confirmed on user_order_confirmed.f_order_id = payment_methods.f_order_id inner join user_order_request on user_order_request.u_order_id = user_order_confirmed.u_order_id where user_order_request.u_order_id = {u_order_id} and is_selected = 1') 
    refund_details_1 = fetch_data(f'select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = delivery_info.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id where user_order_request.u_order_id = {u_order_id}')
    refund_data = fetch_data(f'select * from user_order_request inner join user_order_confirmed on user_order_request.u_order_id = user_order_confirmed.u_order_id inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join purchase_history on delivery_info.transaction_id = purchase_history.transaction_id inner join refund on purchase_history.purchase_history_id = refund.purchase_history_id where user_order_request.u_order_id= {u_order_id};')

    redelivery_data = fetch_data(f'select * from user_order_request inner join user_order_confirmed on user_order_request.u_order_id = user_order_confirmed.u_order_id inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join purchase_history on delivery_info.transaction_id = purchase_history.transaction_id inner join re_delivery on purchase_history.purchase_history_id = re_delivery.purchase_history_id inner join redelivery_info on re_delivery.re_delivery_id = redelivery_info.re_delivery_id where user_order_request.u_order_id= {u_order_id};')
    if redelivery_data:
        pass
    else:
        redelivery_data = fetch_data(f'select * from user_order_request inner join user_order_confirmed on user_order_request.u_order_id = user_order_confirmed.u_order_id inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join purchase_history on delivery_info.transaction_id = purchase_history.transaction_id inner join re_delivery on purchase_history.purchase_history_id = re_delivery.purchase_history_id where user_order_request.u_order_id= {u_order_id};')
            
    for iii in refund_data:
        if iii['is_accepted'] == 1:
            new_refund_data = fetch_data(f'select * from user_order_request inner join user_order_confirmed on user_order_request.u_order_id = user_order_confirmed.u_order_id inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join purchase_history on delivery_info.transaction_id = purchase_history.transaction_id inner join refund on purchase_history.purchase_history_id = refund.purchase_history_id inner join payment_methods_for_refund on refund.refund_id = payment_methods_for_refund.refund_id where user_order_request.u_order_id= {u_order_id};')
            for iiii in new_refund_data:
                if iiii['is_selected'] == 1:
                    new_refund_data = fetch_data(f'select * from user_order_request inner join user_order_confirmed on user_order_request.u_order_id = user_order_confirmed.u_order_id inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join purchase_history on delivery_info.transaction_id = purchase_history.transaction_id inner join refund on purchase_history.purchase_history_id = refund.purchase_history_id inner join payment_methods_for_refund on refund.refund_id = payment_methods_for_refund.refund_id where user_order_request.u_order_id= {u_order_id} and payment_methods_for_refund.is_selected = 1;')
                    refund_data = new_refund_data
                    break

    if payment_methods:
        for things in payment_methods:
            p_id = things['p_id']
        payments_done = fetch_data(f'select * from payments_done where p_id = {p_id}')

        context = {'redelivery_data':redelivery_data,'refund_data':refund_data, 'payments_done':payments_done,'refund_details_1': refund_details_1, 'u_order_id':u_order_id,'data': data, 'delivery_info': delivery_info, 'refund_details':refund_details, 'payment_methods':payment_methods}
    else:
        context = {'redelivery_data':redelivery_data,'refund_data':refund_data,'refund_details_1': refund_details_1, 'u_order_id':u_order_id,'data': data, 'delivery_info': delivery_info, 'refund_details':refund_details, 'payment_methods':payment_methods}
    return render(request, 'view_only_order_details.html', context)

def add_refund(request,f_order_id):
    rf_form = refunddetailsForm(request.POST or None) 
    data = fetch_data(f'select * from user_order_confirmed where f_order_id = {f_order_id}')
    for things in data:
        u_order_id = things['u_order_id']
    context = {'rf_form':rf_form, 'data': data, 'f_order_id':f_order_id}
    if request.method=="POST" and rf_form.is_valid():
        date_status,messageList = check_dateRefund(request.POST["date_from"],request.POST["date_to"],request.POST["refund_percentage"], f_order_id,0)
        if date_status == True:
            rf_form.save()
            save_refund()
            messages.error(request,messageList)
            return redirect('admin_order_update', u_order_id)
        else:
            messages.error(request,messageList)
            return render(request,'add_refund.html', context)
    else:
        return render(request,'add_refund.html', context)

def add_payment_method(request,f_order_id):
    data = fetch_data(f'select * from user_order_confirmed where f_order_id = {f_order_id}')
    pms = payment_methods.objects.filter(for_admin = 1)
    context = {'f_order_id':f_order_id, 'data': data, 'pms':pms}
    for things in data:
        u_order_id = things['u_order_id']
    if request.method =="POST":
        save_pm(request.POST['pm_id'],f_order_id)
        messages.error(request,"Payment Method added")
        return redirect('admin_order_update', u_order_id)
    return render(request,'add_payment_method.html', context)

def update_payment_method(request,p_id):  
    data =fetch_data(f'select * from payment_methods inner join user_order_confirmed on payment_methods.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id where payment_methods.p_id = {p_id}')
    payments_done = fetch_data(f'select * from payments_done where p_id = {p_id}')
    for things in data:
        u_order_id = things['u_order_id']
        is_selected = str(things['is_selected'])

    
    pm_form = paymentmethodsForm(request.POST or None)

    context = {'pm_form':pm_form,'p_id':p_id, 'data': data,'payments_done':payments_done}    
    if request.method == "POST" and pm_form.is_valid():
        #update
        new_payment_method = request.POST["payment_method"]
        new_account_number = request.POST["account_number"]
        new_account_name = request.POST["account_name"]
        dic = {"new_payment_method":new_payment_method,"new_account_number":new_account_number,"new_account_name":new_account_name}
        update_pm(dic,p_id)
        messages.error(request,f"Payment Method has been updated")
        return redirect("admin_order_update", u_order_id)
    return render(request,'update_payment_methods.html',context)

def confirm_payment_amount(request,payment_done_id):
    data = fetch_data(f'select * from payments_done where payment_done_id = {payment_done_id}')
    for things in data:
        p_id = things['p_id']

    context={'data':data}
    if request.method == "POST":
        amount = request.POST['amount_paid']
        payment_for = request.POST['payment_for']
        update_confirm_payment_amount(payment_done_id,payment_for,amount)
        messages.error(request, "Payment Confirmed")
        return redirect('update_payment_method', p_id)
    return render(request, 'confirm_payment_amount.html',context)

def view_payment_done(request, p_id):
    data = fetch_data(f'select * from payments_done where p_id = {p_id}')
    p = fetch_data(f'select * from payment_methods where p_id = {p_id}')
    for ii in p:
        payment_method = ii['payment_method']
    context={'data':data,'payment_method':payment_method}
    return render(request, 'view_payment_done.html', context)

def add_delivery_info(request,f_order_id):
    di_form = deliveryinfoForm(request.POST or None) 
    data = fetch_data(f'select * from user_order_confirmed where f_order_id = {f_order_id}')
    is_paid = fetch_data(f'select * from user_order_confirmed where f_order_id = {f_order_id} and fp_paid = 1')
    shipping_address, contact_info, customer_name= get_shipping_address(f_order_id)
    for things in data:
        u_order_id = things['u_order_id']
    context = {'customer_name':customer_name,'contact_info':contact_info, 'shipping_address':shipping_address,'di_form':di_form,'f_order_id':f_order_id, 'data': data,'is_paid':is_paid,'u_order_id':u_order_id}
    if request.method=="POST" and di_form.is_valid():
        di_form.save()
        save_delivery_info(shipping_address, contact_info, customer_name)
        messages.error(request, "Delivery Info Added")
        return redirect('admin_order_update', u_order_id)
    else:
        return render(request,'add_delivery_info.html', context)


def view_delivery_info(request,f_order_id,u_order_id):
    is_paid = fetch_data(f'select * from user_order_confirmed where f_order_id = {f_order_id} and fp_paid = 1;')
    data = fetch_data(f'select * from delivery_info where f_order_id = {f_order_id}')
    context = {'data': data, 'u_order_id':u_order_id,'f_order_id':f_order_id,'is_paid':is_paid}
    if request.method == 'POST':
        new_delivery_status = request.POST["delivery_status"]
        new_details = request.POST["details"]
        new_date_arrived = request.POST["date_arrived"]
        update_delivery_info(new_delivery_status,new_date_arrived,f_order_id,new_details)
        messages.error(request,"Delivery Info updated successfully")
        return redirect("admin_order_update", u_order_id)
    return render(request, 'view_delivery_info.html',context)

def add_deliv_info(request,f_order_id,u_order_id):
    ugly_date = request.POST['d_date']
    date = request.POST['d_date']
    date = date.split("-")
    date = f'{date[1]}/{date[2]}/{date[0]}'
    task = request.POST['d_details']
    c = f"{date} - {task};"
    data = fetch_data(f'select * from delivery_info where f_order_id = {f_order_id}')
    for ii in data:
        d = ii['details']
    details = f'{d}\n{c}'
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"UPDATE delivery_info set details = '{details}', delivery_status='{task}' where f_order_id = {f_order_id};"
    mycursor.execute(query)
    mydb.commit()
    if "received" in task.lower():
        query2 = f'update delivery_info set delivery_status = "Received", date_arrived = "{ugly_date}" where f_order_id = {f_order_id};'
        mycursor.execute(query2)
        mydb.commit()
        query3 = f"UPDATE user_order_confirmed set is_received = 1 where f_order_id = {f_order_id};"
        mycursor.execute(query3)
        mydb.commit()
    messages.error(request, "Delivery Info added")
    return redirect('view_delivery_info',f_order_id,u_order_id)

def add_redeliv_info(request,re_delivery_id ):
    ugly_date = request.POST['d_date']
    date = request.POST['d_date']
    date = date.split("-")
    date = f'{date[1]}/{date[2]}/{date[0]}'
    task = request.POST['d_details']
    c = f"{date} - {task};"
    data = fetch_data(f'select * from redelivery_info where re_delivery_id = {re_delivery_id}')
    for ii in data:
        d = ii['details']
    details = f'{d}\n{c}'
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"UPDATE redelivery_info set details = '{details}', re_delivery_status ='{task}' where re_delivery_id = {re_delivery_id};"
    mycursor.execute(query)
    mydb.commit()
    if "received" in task.lower():
        query2 = f'update redelivery_info set re_delivery_status = "Received", date_arrived = "{ugly_date}",is_received = 1 where re_delivery_id = {re_delivery_id};'
        mycursor.execute(query2)
        mydb.commit()
        new_data = fetch_data(f'select * from redelivery_info where re_delivery_id = {re_delivery_id};')
        for new in new_data:
            status = new['re_delivery_status']
        query3 =f"update re_delivery set redelivery_status = '{status}' where re_delivery_id = {re_delivery_id};"
        mycursor.execute(query3)
        mydb.commit()

    if "shipped" in task.lower() or "ship" in task.lower():
        query2 = f'update redelivery_info set re_delivery_status = "Shipped", date_shipped = "{ugly_date}" where re_delivery_id = {re_delivery_id};'
        mycursor.execute(query2)
        mydb.commit()
        new_data = fetch_data(f'select * from redelivery_info where re_delivery_id = {re_delivery_id};')
        for new in new_data:
            status = new['re_delivery_status']
        query3 =f"update re_delivery set redelivery_status = '{status}' where re_delivery_id = {re_delivery_id};"
        mycursor.execute(query3)
        mydb.commit()

    messages.error(request, "Delivery Info added")
    return redirect('admin_redelivery_info',re_delivery_id,"update")


def edit_refund_info(request,rd_id):
    data = fetch_data(f"select * from refund_details where rd_id = {rd_id}")
    for things in data:
        f_order_id = int(things['f_order_id'])
    data2 = fetch_data(f'select * from user_order_confirmed where f_order_id = {f_order_id}')
    for things2 in data2:
        u_order_id = things2['u_order_id']
    form = refunddetailsEdit(request.POST or None) 
    context = {'data':data,'form':form, 'rd_id':rd_id,'f_order_id':f_order_id}
    if request.method =="POST" and form.is_valid():
        new_dateto = request.POST["date_to"]
        new_datefrom = request.POST["date_from"]
        new_percentage = f'{request.POST["refund_percentage"]} %'
        date_status,messageList = check_dateRefund(new_datefrom,new_dateto,new_percentage,f_order_id,rd_id)
        if date_status == True:
            update_refund_details(new_dateto,new_datefrom,new_percentage,rd_id)
            messages.error(request,messageList)
            return redirect('admin_order_update', u_order_id)
        else:
            messages.error(request,messageList)
            return render(request, 'edit_refund_info.html',context)
        
    else:
        return render(request, 'edit_refund_info.html',context)

def refund_payment(request, pmfr_id):
    data = fetch_data(f'select * from payment_methods_for_refund inner join refund on payment_methods_for_refund.refund_id = refund.refund_id inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id where pmfr_id = {pmfr_id}')
    for i in data:
        refund_id = i['refund_id']
    form = refundPaymentForm(request.POST, request.FILES)
    context = {'data':data,'form':form}
    if request.method == 'POST' and form.is_valid():
        form.save()
        refund_pay(pmfr_id,refund_id)
        messages.error(request, 'Payment sent')
        return redirect('admin_refund_update',refund_id)
    return render(request,'refund_payment.html',context)

def pay_order_refund(request, pmfr_id):
    data = fetch_data(f'select * from payment_methods_for_refund inner join user_order_confirmed on payment_methods_for_refund.f_order_id_for_refund = user_order_confirmed.f_order_id where pmfr_id = {pmfr_id}')
    for things in data:
        f_order_id = things['f_order_id']

    form = refundPaymentForm(request.POST, request.FILES)
    context = {'data':data,'form':form}
    if request.method == 'POST' and form.is_valid():
        form.save()
        refund_pay_order(pmfr_id,f_order_id)
        messages.error(request, 'Payment sent')
        return redirect('admin_cancelled_orders_details',f_order_id)

    return render(request,'pay_order_refund.html', context)


def admin_redelivery_action(request, re_delivery_id):
    data = fetch_data(f'select * from re_delivery inner join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id inner join user_acc on user_order_request.user_id = user_acc.user_id where re_delivery.re_delivery_id = {re_delivery_id};')
    context={'data': data}
    set_quantity_to_inactive()
    if request.method == 'POST':
        accept_redelivery(re_delivery_id)
        messages.error(request, 'Re-delivery Request has been Accepted')
        return redirect('admin_redelivery_requests')
    return render(request, 'admin_redelivery_action.html', context)

def admin_redelivery_update(request, re_delivery_id):
    data = fetch_data(f'select * from re_delivery inner join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id where re_delivery.re_delivery_id = {re_delivery_id};')
    for ii in data:
        quantity_selected = ii['quantity_variations_id']
        grade_selected = ii['grade']
    harvest_id = get_harvest_id(re_delivery_id)
    rd_info = fetch_data(f'select * from redelivery_info inner join batch_quantity_variations on redelivery_info.quantity_variations_id = batch_quantity_variations.quantity_id where redelivery_info.re_delivery_id = {re_delivery_id}')
    quantities = fetch_data(f'select * from batch_quantity_variations where harvest_id = {harvest_id} and quantity_id = {quantity_selected}')
    batch_data = fetch_data(f'select * from batch_harvest inner join plant_batch on batch_harvest.batch_id = plant_batch.batch_id inner join plant_profile on plant_batch.plant_id = plant_profile.plant_id where batch_harvest.harvest_id = {harvest_id}')
    
    plant_name = get_plant_name(data)
    context={'grade_selected':grade_selected,'quantity_selected':quantity_selected,'plant_name':plant_name,'data': data, 'rd_info':rd_info,'re_delivery_id':re_delivery_id,'harvest_id':harvest_id, 'quantities':quantities,'batch_data':batch_data}
    return render(request, 'admin_redelivery_update.html',context)

def get_plant_name(data):
    for things in data:
        a = things['plant_name']
    return a
def admin_redelivery_details(request, harvest_id, re_delivery_id,quantity_selected):

    data = fetch_data(f"select * from batch_harvest inner join plant_batch on batch_harvest.batch_id = plant_batch.batch_id inner join plant_profile on plant_batch.plant_id = plant_profile.plant_id where batch_harvest.harvest_id = {harvest_id};")
    quantities = fetch_data(f"select * from batch_quantity_variations where batch_quantity_variations.harvest_id = {harvest_id} and batch_quantity_variations.quantity_id = {quantity_selected};")
    returned_quantity = fetch_data(f'select returned_quantity from re_delivery where re_delivery_id ={re_delivery_id};')
    form = redeliverydetailsForm(request.POST or None)
    context = {'form':form,'data':data,'quantities':quantities,'returned_quantity':returned_quantity}
    
    
    if request.method == "POST" and form.is_valid():
        form.save()
        quan_delivered = request.POST['quantity_delivered']
        quan_id = request.POST['quantity_variations_id']
        confirm__redelivery_details(re_delivery_id)
        update_quantity(quan_id,quan_delivered)
        messages.error(request,"Redelivery Details Saved")
        return redirect('admin_redelivery_update',re_delivery_id)
    
    return render(request,'admin_redelivery_details.html',context )


def admin_redelivery_info(request, re_delivery_id, status):
    shipping_address, contact_info, customer_name = get_shipping_address2(re_delivery_id)
    data = fetch_data(f'select * from redelivery_info where re_delivery_id = {re_delivery_id}')
    form = redeliveryUpdateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        if status == "add":
            form.save()
            add_db_redelivery_info(re_delivery_id, shipping_address,contact_info, customer_name)
            messages.error(request, "Redelivery Info Saved")
            return redirect('admin_redelivery_update',re_delivery_id)
        elif status == "update":
            update_db_redelivery_info(request, re_delivery_id)
            messages.error(request, "Redelivery Info Updated")
            return redirect('admin_redelivery_update',re_delivery_id)
    context = {'customer_name':customer_name, 'contact_info':contact_info ,'form':form, 'data':data, 'status':status,'shipping_address':shipping_address}
    return render(request,'admin_redelivery_info.html',context )

def announcements_admin(request):
    check_announcement_date_remaning()
    data = fetch_data(f'select * from announcements where remove_to_view = 0;')
    context = {'data':data}
    if request.method == "POST":
        data = filter_announcements(request.POST['submit'])
        context = {'data':data}
        return render(request, 'announcements_admin.html', context)
    else:
        return render(request, 'announcements_admin.html', context)

def add_announcement(request,action,a_id):
    data = fetch_data(f'select * from announcements where a_id = {a_id}')
    form = announcementForm(request.POST or None)
    context= {'data':data,'a_id':a_id}
    if action == "edit":
        if request.method == "POST" and form.is_valid():
            update_announcement_db(request, a_id)
            messages.error(request, 'Announcement has been Updated')
            return redirect('announcements_admin')
    else:
        if request.method == "POST" and form.is_valid():
            form.save()
            add_announcement_db()
            messages.error(request, 'Announcement has been published')
            return redirect('announcements_admin')
    return render(request, 'add_announcement.html', context)

def remove_to_view(request,rtv_type,some_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    if rtv_type == "order":
        query = f"UPDATE user_order_request set remove_to_view = 1 where u_order_id = {some_id};"
        mycursor.execute(query)
        mydb.commit()
        return redirect('admin_order_requests')
    elif rtv_type == "redelivery":
        query = f"UPDATE re_delivery set remove_to_view = 1 where re_delivery_id = {some_id};"
        mycursor.execute(query)
        mydb.commit()
        return redirect('admin_redelivery_requests')
    elif rtv_type == "cancelled":
        query = f"UPDATE user_order_confirmed set cancelled_remove_to_view = 1 where u_order_id = {some_id};"
        mycursor.execute(query)
        mydb.commit()
        return redirect('admin_cancelled_orders')
    elif rtv_type == "refund":
        query = f"UPDATE refund set remove_to_view = 1 where refund_id = {some_id};"
        mycursor.execute(query)
        mydb.commit()
        return redirect('admin_refund_requests')
    elif rtv_type == "announcements":
        query = f"UPDATE announcements set remove_to_view = 1 where a_id = {some_id};"
        mycursor.execute(query)
        mydb.commit()
        return redirect('announcements_admin')
    
    

def back_to_view(request,rtv_type, some_id):
    mydb = mysql.connector.connect(
        host ="localhost",
        user="root",
        password="root",
        database="farmsys",
        )
    mycursor = mydb.cursor(dictionary=True)
    if rtv_type == "order":
        query = f"UPDATE user_order_request set remove_to_view = 0 where u_order_id = {some_id};"
        mycursor.execute(query)
        mydb.commit()
        return redirect('removed_from_view', 'order')
    elif rtv_type == "redelivery":
        query = f"UPDATE re_delivery set remove_to_view = 0 where re_delivery_id = {some_id};"
        mycursor.execute(query)
        mydb.commit()
        return redirect('removed_from_view', 'redelivery')
    elif rtv_type == "cancelled":
        query = f"UPDATE user_order_confirmed set cancelled_remove_to_view = 0 where u_order_id = {some_id};"
        mycursor.execute(query)
        mydb.commit()
        return redirect('removed_from_view', 'cancelled')
    elif rtv_type == "refund":
        query = f"UPDATE refund set remove_to_view = 0 where refund_id = {some_id};"
        mycursor.execute(query)
        mydb.commit()
        return redirect('removed_from_view','refund')
    elif rtv_type == "announcements":
        query = f"UPDATE announcements set remove_to_view = 0 where a_id = {some_id};"
        mycursor.execute(query)
        mydb.commit()
        return redirect('removed_from_view','announcements')
    

def removed_from_view(request, r_type):
    if r_type == "order":
        data  = fetch_data("select * from user_order_request left join batch_quantity_variations on user_order_request.quantity_variations_id =batch_quantity_variations.quantity_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select user_order_confirmed.u_order_id as rd_ready_id, refund_details.rd_id as rd_ready from user_order_confirmed left join refund_details on user_order_confirmed.f_order_id = refund_details.f_order_id limit 1) as rd_ready on user_order_request.u_order_id = rd_ready.rd_ready_id left join (select user_order_confirmed.u_order_id as di_ready_id, delivery_info.transaction_id as di_ready from user_order_confirmed left join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id limit 1) as di_ready on user_order_request.u_order_id = di_ready.di_ready_id left join (select user_order_confirmed.u_order_id as pm_ready_id, payment_methods.p_id as pm_ready from user_order_confirmed left join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id limit 1) as pm_ready on user_order_request.u_order_id = pm_ready.pm_ready_id where user_order_request.remove_to_view = 1")
        context = {'data' : data, 'rtype': r_type}
        if request.method == "POST":
            order_by = request.POST['submit']
            if order_by == "full_name":
                data = fetch_data(f"select * from user_order_request left join batch_quantity_variations on user_order_request.quantity_variations_id =batch_quantity_variations.quantity_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select user_order_confirmed.u_order_id as rd_ready_id, refund_details.rd_id as rd_ready from user_order_confirmed left join refund_details on user_order_confirmed.f_order_id = refund_details.f_order_id limit 1) as rd_ready on user_order_request.u_order_id = rd_ready.rd_ready_id left join (select user_order_confirmed.u_order_id as di_ready_id, delivery_info.transaction_id as di_ready from user_order_confirmed left join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id limit 1) as di_ready on user_order_request.u_order_id = di_ready.di_ready_id left join (select user_order_confirmed.u_order_id as pm_ready_id, payment_methods.p_id as pm_ready from user_order_confirmed left join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id limit 1) as pm_ready on user_order_request.u_order_id = pm_ready.pm_ready_id where user_order_request.remove_to_view = 1 order by user_acc.{order_by}")
            else:
                if order_by == "u_order_id":
                    data = fetch_data(f"select * from user_order_request left join batch_quantity_variations on user_order_request.quantity_variations_id =batch_quantity_variations.quantity_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select user_order_confirmed.u_order_id as rd_ready_id, refund_details.rd_id as rd_ready from user_order_confirmed left join refund_details on user_order_confirmed.f_order_id = refund_details.f_order_id limit 1) as rd_ready on user_order_request.u_order_id = rd_ready.rd_ready_id left join (select user_order_confirmed.u_order_id as di_ready_id, delivery_info.transaction_id as di_ready from user_order_confirmed left join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id limit 1) as di_ready on user_order_request.u_order_id = di_ready.di_ready_id left join (select user_order_confirmed.u_order_id as pm_ready_id, payment_methods.p_id as pm_ready from user_order_confirmed left join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id limit 1) as pm_ready on user_order_request.u_order_id = pm_ready.pm_ready_id where user_order_request.remove_to_view = 1 order by user_order_request.{order_by} desc")
                else:
                    data = fetch_data(f"select * from user_order_request left join batch_quantity_variations on user_order_request.quantity_variations_id =batch_quantity_variations.quantity_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select user_order_confirmed.u_order_id as rd_ready_id, refund_details.rd_id as rd_ready from user_order_confirmed left join refund_details on user_order_confirmed.f_order_id = refund_details.f_order_id limit 1) as rd_ready on user_order_request.u_order_id = rd_ready.rd_ready_id left join (select user_order_confirmed.u_order_id as di_ready_id, delivery_info.transaction_id as di_ready from user_order_confirmed left join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id limit 1) as di_ready on user_order_request.u_order_id = di_ready.di_ready_id left join (select user_order_confirmed.u_order_id as pm_ready_id, payment_methods.p_id as pm_ready from user_order_confirmed left join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id limit 1) as pm_ready on user_order_request.u_order_id = pm_ready.pm_ready_id where user_order_request.remove_to_view = 1 order by user_order_request.{order_by}")
            context ={'data':data, 'rtype': r_type}
            return render(request, 'removed_from_view.html', context)
        else:
         return render(request,'removed_from_view.html', context)
    if r_type == "redelivery":
        data = fetch_data("select * from re_delivery left join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id left join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id left join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select redelivery_info.re_delivery_id as rdo_ready,redelivery_info.re_delivery_status as rdi_ready from redelivery_info left join re_delivery on redelivery_info.re_delivery_id = re_delivery.re_delivery_id) as rd_ready on rd_ready.rdo_ready = re_delivery.re_delivery_id where re_delivery.remove_to_view = 1;")
        context = {'data' : data, 'rtype': r_type}
        if request.method=="POST":
            order_by = request.POST['submit']
            if order_by in ["redelivery_status","is_accepted","request_date"]:
                data =fetch_data(f'select * from re_delivery left join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id left join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id left join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select redelivery_info.re_delivery_id as rdo_ready,redelivery_info.re_delivery_status as rdi_ready from redelivery_info left join re_delivery on redelivery_info.re_delivery_id = re_delivery.re_delivery_id) as rd_ready on rd_ready.rdo_ready = re_delivery.re_delivery_id where re_delivery.remove_to_view = 1 order by re_delivery.{order_by}')
                if order_by == "request_date":
                    data =fetch_data(f'select * from re_delivery left join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id left join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id left join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select redelivery_info.re_delivery_id as rdo_ready,redelivery_info.re_delivery_status as rdi_ready from redelivery_info left join re_delivery on redelivery_info.re_delivery_id = re_delivery.re_delivery_id) as rd_ready on rd_ready.rdo_ready = re_delivery.re_delivery_id where re_delivery.remove_to_view = 1 order by re_delivery.{order_by} desc')
                context ={'data':data, 'rtype': r_type}
                return render(request, 'removed_from_view.html', context)
            else:
                if order_by == "full_name":
                    data =fetch_data(f'select * from re_delivery left join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id left join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id left join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select redelivery_info.re_delivery_id as rdo_ready,redelivery_info.re_delivery_status as rdi_ready from redelivery_info left join re_delivery on redelivery_info.re_delivery_id = re_delivery.re_delivery_id) as rd_ready on rd_ready.rdo_ready = re_delivery.re_delivery_id where re_delivery.remove_to_view = 1 order by user_acc.{order_by}')
                elif order_by == 'u_order_id':
                    data =fetch_data(f'select * from re_delivery left join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id left join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id left join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select redelivery_info.re_delivery_id as rdo_ready,redelivery_info.re_delivery_status as rdi_ready from redelivery_info left join re_delivery on redelivery_info.re_delivery_id = re_delivery.re_delivery_id) as rd_ready on rd_ready.rdo_ready = re_delivery.re_delivery_id where re_delivery.remove_to_view = 1 order by user_order_request.{order_by} desc')
                else:
                    data =fetch_data(f'select * from re_delivery left join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id left join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id left join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select redelivery_info.re_delivery_id as rdo_ready,redelivery_info.re_delivery_status as rdi_ready from redelivery_info left join re_delivery on redelivery_info.re_delivery_id = re_delivery.re_delivery_id) as rd_ready on rd_ready.rdo_ready = re_delivery.re_delivery_id where re_delivery.remove_to_view = 1 order by user_order_request.{order_by}')
                context ={'data':data, 'rtype': r_type}
                return render(request, 'removed_from_view.html', context)
        else:
            return render(request, 'removed_from_view.html', context)
        
    elif r_type == "cancelled":
        data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id  where is_cancelled = 1 and cancelled_remove_to_view = 1;')
        context = {'data' : data, 'rtype': r_type}
        if request.method == "POST":
            order_by = request.POST['submit']
            if order_by == "full_name":
                data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id  where is_cancelled = 1 and cancelled_remove_to_view = 1; by user_acc.{order_by};')
            elif order_by == "u_order_id":
                data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id  where is_cancelled = 1 and cancelled_remove_to_view = 1; order by user_order_request.{order_by} desc; ')
            elif order_by == "plant_name":
                data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id  where is_cancelled = 1 and cancelled_remove_to_view = 1; order by user_order_request.{order_by};')
            elif order_by == "refund_date":
                data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id  where is_cancelled = 1 and cancelled_remove_to_view = 1; order by user_order_confirmed.{order_by};')
            elif order_by == "cancel_date":
                data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id  where is_cancelled = 1 and cancelled_remove_to_view = 1; order by user_order_confirmed.{order_by} desc;')
            context={'data':data, 'rtype': r_type}
            return render(request,'removed_from_view.html',context)
        else:
            return render(request,'removed_from_view.html',context)

    elif r_type == "announcements":
        data = fetch_data(f'select * from announcements where remove_to_view = 1;')
        context = {'data' : data, 'rtype': r_type}
        if request.method == "POST":
            order_by = request.POST['submit']
            if order_by in ["a_date_published" , "a_days","a_status"]:
                data = fetch_data(f'select * from announcements where remove_to_view = 1 order by {order_by} desc;')
                context = {'data':data, 'rtype': r_type}
                return render(request, 'removed_from_view.html', context)
            else:
                data = fetch_data(f'select * from announcements where remove_to_view = 1 order by {order_by};')
                context = {'data':data, 'rtype': r_type}
                return render(request, 'removed_from_view.html', context)
        else:
            return render(request, 'removed_from_view.html', context)

    elif r_type == "refund":
        data = fetch_data("select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.remove_to_view = 1")
        context = {'data': data, 'rtype': r_type}
        if request.method == "POST":
            order_by = request.POST['submit']
            if order_by == "full_name":
                data = fetch_data(f"select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.remove_to_view = 1 order by user_acc.{order_by}")
            elif order_by in ['request_date','is_accepted','refund_amount']:
                if order_by == "request_date":
                    data = fetch_data(f"select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.remove_to_view = 1 order by refund.{order_by} desc")
                else:
                    data = fetch_data(f"select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.remove_to_view = 1 order by refund.{order_by}")
            else:
                if order_by == "u_order_id":
                    data = fetch_data(f"select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.remove_to_view = 1 order by user_order_request.{order_by} desc")
                else:    
                    data = fetch_data(f"select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.remove_to_view = 1 order by user_order_request.{order_by}")
            context = {'data': data, 'rtype': r_type}
            return render(request, 'removed_from_view.html', context)
        else:
            return render(request, 'removed_from_view.html', context)

def received_orders(request):
    data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id where user_order_confirmed.is_received = 1 and payment_methods.is_selected = 1')
    if request.method == "POST":
        data = filter_received_orders(request.POST['submit'])
        context = {'data':data}
        return render(request, 'received_orders.html', context)
    else:
        context = {'data':data}
        return render(request, 'received_orders.html', context)

def admin_payment_methods(request):
    data = payment_methods.objects.filter(for_admin = 1) 
    if request.method == "POST":
        data = data.order_by(request.POST['submit'])
    context = {"data":data}
    update_pma_db()
    return render(request, 'admin_payment_methods.html', context)

def add_admin_payment_method(request, add_type, p_id):
    if add_type == "edit":
        data = payment_methods.objects.get(id = p_id)
        context = {'data':data,'add_type':add_type}
        if request.method == "POST":
            if request.POST['payment_method'].lower() in ['gcash', 'paymaya']:
                is_valid = validate_phone(request.POST['account_number'])
                if is_valid == False:
                    messages.error(request, 'Invalid Account number, please double check')
                    return redirect('add_admin_payment_method',add_type, p_id)
            if request.POST['payment_method'].lower() == "paypal":
                is_valid2 = validate_email(request.POST['account_number'])
                if is_valid2 == False:
                    messages.error(request, 'Invalid Account number, please double check')
                    return redirect('add_admin_payment_method',add_type, p_id)

            data.payment_method = request.POST['payment_method']
            data.account_name = request.POST['account_name']
            data.account_number = request.POST['account_number']
            data.save()
            messages.error(request, "Payment Method has been updated")
            return redirect('admin_payment_methods')
        return render(request, 'add_admin_payment_method.html',context)
    else:
        data = "yes"
        form = adminpaymentmethodsForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            if request.POST['payment_method'].lower() in ['gcash', 'paymaya']:
                is_valid = validate_phone(request.POST['account_number'])
                if is_valid == False:
                    messages.error(request, 'Invalid Account number, please double check')
                    return redirect('add_admin_payment_method',add_type, p_id)
            if request.POST['payment_method'].lower() == "paypal":
                is_valid2 = validate_email(request.POST['account_number'])
                if is_valid2 == False:
                    messages.error(request, 'Invalid Account number, please double check')
                    return redirect('add_admin_payment_method',add_type, p_id)
            form.save()
            messages.error(request, "Payment Method has been saved")
            return redirect('admin_payment_methods')
        return render(request, 'add_admin_payment_method.html',{"data":data})

def sales_summary(request):
    data = fetch_data('select user_order_confirmed.u_order_id ,user_order_confirmed.confirmed_quantity, user_order_confirmed.units, user_order_confirmed.total_amount, user_order_confirmed.delivery_fee, user_order_confirmed.dp_status, user_order_confirmed.fullpayment_status ,payment_methods.payment_method ,payment_methods.account_name ,payment_methods.total_amount_paid ,user_order_confirmed.cancel_date ,user_order_confirmed.cancel_refund_amount, user_order_confirmed.is_cancelled, refund.refund_amount, re_delivery.returned_quantity, batch_quantity_variations.price_per_unit, payment_done.date_paid from user_order_confirmed left join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id left join (select max(date_paid) as date_paid, p_id from payments_done group by p_id) as payment_done on payment_methods.p_id = payment_done.p_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id left join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id left join purchase_history on delivery_info.transaction_id = purchase_history.transaction_id left join refund on purchase_history.purchase_history_id = refund.purchase_history_id left join re_delivery on purchase_history.purchase_history_id = re_delivery.purchase_history_id where payment_methods.is_selected = 1 or refund.is_accepted = 1 or re_delivery.is_accepted = 1 order by user_order_request.u_order_id')
    someword = "asd"
    if request.method == "POST":
        m, y = get_filter_date(request.POST['months'])
        someword = request.POST['months']
        data = fetch_data(f"select user_order_confirmed.u_order_id ,user_order_confirmed.confirmed_quantity, user_order_confirmed.units, user_order_confirmed.total_amount, user_order_confirmed.delivery_fee, user_order_confirmed.dp_status, user_order_confirmed.fullpayment_status ,payment_methods.payment_method ,payment_methods.account_name ,payment_methods.total_amount_paid ,user_order_confirmed.cancel_date ,user_order_confirmed.cancel_refund_amount, user_order_confirmed.is_cancelled, refund.refund_amount, re_delivery.returned_quantity, batch_quantity_variations.price_per_unit, payment_done.date_paid from user_order_confirmed left join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id inner join (select max(date_format(str_to_date(date_paid, '%Y-%m-%d'), '%Y-%m-%d')) as date_paid, p_id from payments_done where month(date_paid) = {m} and year(date_paid) = {y} group by p_id) as payment_done on payment_methods.p_id = payment_done.p_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join batch_quantity_variations on user_order_request.quantity_variations_id = batch_quantity_variations.quantity_id left join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id left join purchase_history on delivery_info.transaction_id = purchase_history.transaction_id left join refund on purchase_history.purchase_history_id = refund.purchase_history_id left join re_delivery on purchase_history.purchase_history_id = re_delivery.purchase_history_id where payment_methods.is_selected = 1 or refund.is_accepted = 1 or re_delivery.is_accepted = 1")
    context ={'data':data, 'someword':someword}
    return render(request, 'sales_summary.html', context)


def get_filter_date(a):
    a = a.split("-")
    return int(a[1]), int(a[0])


def refund_rules(request):
    '''
    given that gap > 7 days <=15:
    1st day = 75% refund
    2-3th day = 50% refund
    4-5th day = 25% refund
    6th day onwards = 0%

    if gap =< 7 days:
    1st day = 50%
    2-4th = 25%
    5-7th = 0%

    gap < 15 days
    1-2nd day = 100%
    3-6th = 75%
    7-9th = 50%
    10-12th = 25%
    13th day + = 0%
    '''
    return render(request, 'refund_rules.html', {})


########################################################################

############################################################

'''
def growth_details(request):
    return render(request,"growth_details.html", {})
'''

############################################################



class CalendarView(generic.ListView):
    model = Event
    template_name = 'growth_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['a'] = self.request.GET.get('day', None)
        return context





def growth_details(request, batch_id):

    first_date = fetch_data(f'select min(date_from) as date from plant_monitoring  where batch_id = {batch_id}') #getting the earliest date sa monitoring
    for date in first_date:
        try:
            fdate = date['date'].strftime('%Y-%m-%d')
        except:
            new_date = date['date'].split("T")[0]
            fdate = datetime.strptime(new_date, '%Y-%m-%d')
            fdate = fdate.strftime('%Y-%m-%d')

    d = get_date(fdate)

    cal = Calendar(d.year, d.month, batch_id)
    html_cal = cal.formatmonth(withyear=True)
    calendar = mark_safe(html_cal)
    
    # ipass ang current date para kabalo sya when mag next 
    
    context = {'calendar': calendar, 'date': fdate, 'batch_id': batch_id}
    return render(request, 'growth_details.html', context)



def next_month(request, curr_date, batch_id):
    try:
        curr_date = datetime.strptime(curr_date, '%Y-%m-%d %H:%M:%S') + relativedelta(months=1) #weird error na usahay lang mahitabo na naay uncoverted minutes and seconds
    except:
        curr_date = datetime.strptime(curr_date, '%Y-%m-%d') + relativedelta(months=1)
    d = curr_date

    cal = Calendar(d.year, d.month, batch_id)
    html_cal = cal.formatmonth(withyear=True)
    calendar = mark_safe(html_cal) 
    
    # ipass ang current date para kabalo sya when mag next 
    
    context = {'calendar': calendar, 'date': curr_date, 'batch_id': batch_id}
    return render(request, 'growth_details.html', context) 


def prev_month(request, curr_date, batch_id):
    try:
        curr_date = datetime.strptime(curr_date, '%Y-%m-%d %H:%M:%S') + relativedelta(months=-1) #weird error na usahay lang mahitabo na naay uncoverted minutes and seconds
    except:
        curr_date = datetime.strptime(curr_date, '%Y-%m-%d') + relativedelta(months=-1)
    d = curr_date

    cal = Calendar(d.year, d.month, batch_id)
    html_cal = cal.formatmonth(withyear=True)
    calendar = mark_safe(html_cal)
    
    # ipass ang current date para kabalo sya when mag next 
    
    context = {'calendar': calendar, 'date': curr_date, 'batch_id': batch_id}
    return render(request, 'growth_details.html', context)

def get_date(req_day): #diri agi-on ang pag select sa date
    if req_day:
        ddate = req_day.split('-')
        year = int(ddate[0])
        month = int(ddate[1])
        return date(year, month, day=1)
    return datetime.today() #return the current date today

'''

def get_date(req_day): #diri agi-on ang pag select sa date
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today() #return the current date today

    #date = "2022-07-01 12:12:12.123456" #select a specific date... never mind lang ang time kay ang date lang ang need pero ibutang lang gihapon ang time
    #date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    #return date

'''
'''
def growth_details(request, batch_id):
    d = get_date(None)

    cal = Calendar(d.year, d.month)
    html_cal = cal.formatmonth(withyear=True)
    calendar = mark_safe(html_cal)
    context = {'calendar': calendar}
    return render(request, 'growth_details.html', context)
'''

###########FUNCTIONS##############
def validate_data_phone(phone,a,b):
    error= ""
    error2= ""
    boo = validate_phone(phone)
    boo2 = validate_pass(a,b)
    if boo == False:
        error = "INVALID Phone Format please use (+63)"
    if boo2 == False:
        error2 = 'ERROR: Password does not Match!'

    err_mess = [error, error2]
    if boo == False:
        return False, err_mess
    elif boo2 == False:
        return False, err_mess
    else:
        return True, err_mess

def validate_data_email(email,a,b):
    error= ""
    error2= ""
    boo = validate_email(email)
    boo2 = validate_pass(a,b)
    if boo == False:
        error = "INVALID Email Format must containt @ and end in .com"
    if boo2 == False:
        error2 = 'ERROR: Password does not Match!'

    err_mess = [error, error2]
    if boo == False:
        return False, err_mess
    elif boo2 == False:
        return False, err_mess
    else:
        return True, err_mess

def validate_email(email):
    regx = r'^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$'
    err_mess = ""
    if re.match(regx,str(email)):
        return True
    else:
        return False

def validate_phone(num):
    regx = r'^(09|\+639)\d{9}$'
    if re.match(regx,str(num)):
        return True
    else:
        return False

def validate_pass(a,b):
    err_mess = "None"
    if str(a) != str(b):
        return False
    else:
        return True




def fetch_data(query):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult 

def save_user(new_data):
    user_id = new_data.id
    username = new_data.username
    passw  = new_data.passw
    confirm_passw = new_data.confirm_passw
    phone_num= new_data.phone_num
    email_ad = new_data.email_ad
    
    if new_data.is_authenticated == True:
        is_authenticated = 1
    else:
        is_authenticated = 0

    full_name = new_data.full_name
    comp = new_data.comp
    adress = new_data.adress
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",


       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"Insert into user_acc(user_id, username,pass,phone_num,email_ad,is_authenticated, full_name,company,socials) values({user_id},'{username}','{passw}','{phone_num}','{email_ad}',{is_authenticated},'{full_name}','{comp}','{adress}');"
    #query = f"Insert into user_acc(user_id, username,pass,phone_num,email_ad,is_authenticated, full_name,company,socials) values({int(user_id)},{str(username)},{str(passw)},{str(phone_num)},{str(email_ad)},{int(is_authenticated)},{str(full_name)},{str(comp)},{str(adress)});"
    mycursor.execute(query)
    mydb.commit()

def get_user_id(username):
    user_id = fetch_data(f"select user_id from user_acc where user_acc.username = '{username}';")
    for things in user_id:
        user_id = user_id[0]
    return user_id["user_id"]



def save_data(new_data):
    date = str(datetime.now().date())
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    orderID = new_data.id
    user_id = new_data.user_id
    plant_name = new_data.plant_name
    quantity = new_data.quantity
    date_needed = new_data.date_needed 
    is_admin_approved = new_data.is_admin_approved 
    harvest_id = new_data.harvest_id 
    quantity_variations_id = new_data.quantity_variations_id 


    query = f"Insert into user_order_request(u_order_id,user_id, plant_name,quantity,date_needed,is_admin_approved,harvest_id, quantity_variations_id, order_request_date) values({orderID},'{user_id}','{plant_name}','{quantity}','{date_needed}',{is_admin_approved},'{harvest_id}','{quantity_variations_id}','{date}');"
    mycursor.execute(query)
    mydb.commit()


def cancel_order(reason, f_order_id):
    date = str(datetime.now().date())
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"UPDATE user_order_confirmed set is_cancelled = 1, cancel_reason = '{reason}', cancel_date = '{date}' where f_order_id = {f_order_id};"
    mycursor.execute(query)
    mydb.commit()
    calculate_refund_amount(f_order_id,date)

def calculate_refund_amount(f_order_id,date):
    payment = fetch_data(f'select * from payment_methods where f_order_id = {f_order_id} and is_selected = 1;')
    data = fetch_data(f'select * from user_order_confirmed where f_order_id = {f_order_id};')
    refunds = fetch_data(f'select * from refund_details where f_order_id = {f_order_id}')

    quantity_variation = fetch_data(f'select * from batch_quantity_variations inner join user_order_request on batch_quantity_variations.quantity_id = user_order_request.quantity_variations_id inner join user_order_confirmed on user_order_request.u_order_id = user_order_confirmed.u_order_id where user_order_confirmed.f_order_id = {f_order_id};')

    for i in data:
        quan_confirmed = i['confirmed_quantity'] 
    for ii in quantity_variation:
        curr_quan = ii['quantity_harvested']
        quan_id = ii['quantity_variations_id']

    new_quantity = float(quan_confirmed) + float(curr_quan)

    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"update batch_quantity_variations set quantity_harvested ='{new_quantity}' where quantity_id = {quan_id};"
    mycursor.execute(query)
    mydb.commit()
    get_refund_amount(payment, f_order_id, refunds,date)
    

def get_refund_amount(payment, f_order_id, refunds,date):
    refund_amount = 0
    total_payment = 0
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    for ii in payment:
        total_payment = float(ii['total_amount_paid'])
    for i in refunds:
        if datetime.strptime(i['date_from'], '%Y-%m-%d') <= datetime.strptime(date, '%Y-%m-%d') <= datetime.strptime(i['date_to'], '%Y-%m-%d'):
            #do somethings
            refund_percentage = float(i['refund_percentage'].split(" ")[0])/100
            refund_amount =  total_payment * refund_percentage

    query = f"update user_order_confirmed set cancel_refund_amount ='{refund_amount}' where f_order_id = {f_order_id};"
    mycursor.execute(query)
    mydb.commit()        





def update_db_payment():
    date = str(datetime.now().date())
    payment = payments.objects.last()
    payments_done_id = payment.id
    p_id = payment.p_id
    payment_for = payment.payment_for
    receipt = payment.proof_receipt
    amount_paid = payment.amount_paid
    link = get_img_link(receipt)
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"UPDATE payment_methods set is_selected = 1 where p_id = {p_id};"
    query2 = f'insert into payments_done(payment_done_id, p_id,payment_for,amount_paid,proof_of_payment,date_paid,is_confirmed) values({payments_done_id}, {p_id}, "{payment_for}","{amount_paid}","{link}","{date}", 0);'
    mycursor.execute(query)
    mydb.commit()
    mycursor.execute(query2)
    mydb.commit()
    remove_not_selected_method(p_id)

def remove_not_selected_method(p_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    data = fetch_data(f'select * from payment_methods where p_id = {p_id}')
    for ii in data:
        f_order_id = ii['f_order_id']
    data2 = fetch_data(f'select * from payment_methods where f_order_id = {f_order_id}')
    for things in data2:
        if str(things['is_selected']) == "0":
            query = f"delete from payment_methods where p_id = {int(things['p_id'])}"
            mycursor.execute(query)
            mydb.commit()
            mycursor = mydb.cursor(dictionary=True)
            



def update_confirm_payment_amount(payment_done_id,payment_for,amount):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"UPDATE payments_done set is_confirmed = 1,payment_for ='{payment_for}', amount_paid ='{amount}' where payment_done_id = {payment_done_id};"
    mycursor.execute(query)
    mydb.commit()


    data = fetch_data(f'select * from payments_done where payment_done_id = {payment_done_id};')
    for i in data:
        p_id = i['p_id']
    data2 = fetch_data(f'select * from payment_methods where p_id = {p_id}')
    for ii in data2:
        total_amount_paid = ii['total_amount_paid']

    new_total_amount_paid = float(total_amount_paid) + float(amount)
    query2 = f'UPDATE payment_methods set total_amount_paid = {new_total_amount_paid} where p_id = {p_id}'
    mycursor.execute(query2)
    mydb.commit()

    update_balance_to_pay(p_id, amount)



def update_balance_to_pay(p_id, amount):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    data = fetch_data(f'select * from payment_methods where p_id = {p_id}')
    for i in data:
        f_order_id = i['f_order_id']
        total_payment = float(i['total_amount_paid'])
    data2 = fetch_data(f'select * from user_order_confirmed where f_order_id = {f_order_id}')
    for ii in data2:
        balance_to_pay = float(ii['balance_to_pay'])
        total_downpayment = float(ii['total_downpayment'])
        total_to_pay = float(ii['total_amount']) + float(ii['delivery_fee'])

    dp_paid = 0
    fp_paid = 0
    if total_payment >= total_downpayment:
        dp_paid = 1
    else:
        dp_paid = 0

    if total_payment >= total_to_pay:
        fp_paid = 1 
    else:
        fp_paid = 0 

    new_balance_to_pay = balance_to_pay - float(amount)

    query = f"update user_order_confirmed set balance_to_pay='{new_balance_to_pay}', dp_paid = {dp_paid}, fp_paid ={fp_paid} where f_order_id = {f_order_id};"
    mycursor.execute(query)
    mydb.commit()



def send_redelivery():
    date = str(datetime.now().date())
    redelivery = req_redelivery.objects.last()
    link = get_img_link(redelivery.proof_pic)

    
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"insert into re_delivery(re_delivery_id, purchase_history_id, reason_for_redelivery, returned_quantity, units, proof_img, request_date) values('{redelivery.id}','{redelivery.transac_id}','{redelivery.reason_rd}','{redelivery.returned_quan}','{redelivery.units}','{link}','{date}');"
    
    query2 = f"UPDATE purchase_history set quantity_received = '{redelivery.quan_received}' where purchase_history_id = {redelivery.transac_id};"
    mycursor.execute(query)
    mydb.commit()
    mycursor.execute(query2)
    mydb.commit()

def send_refund():   
    date = str(datetime.now().date())
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    refund = req_refund.objects.last()
    link = get_img_link(refund.proof_refund)
    mycursor = mydb.cursor(dictionary=True)
    query = f"insert into refund(refund_id, purchase_history_id, reason_for_refund, returned_quantity, units, proof_refund, request_date)values('{refund.id}','{refund.transac_id}','{refund.reason_refund}','{refund.refund_quan}','{refund.units}','{link}','{date}');"
    
    query2 = f"UPDATE purchase_history set quantity_received = '{refund.quantity_received}' where purchase_history_id = {refund.transac_id};"

    mycursor.execute(query)
    mydb.commit()
    mycursor.execute(query2)
    mydb.commit()




def get_img_link(receipt):
    CLIENT_ID = '851c881d15a628e'
    CLIENT_SECRET = 'de18eba31b31c91cc3134f1bea74c39b80e099ed'
    imgr_username = "rheejan"   
    imgr_password = "09491751465"

    client = ImgurClient(CLIENT_ID, CLIENT_SECRET)

    auth_url = client.get_auth_url('pin')

    #PATH =f'../images/{receipt}'
    PATH = f'{Path().absolute()}/images/{receipt}' 
    album=  None

    config={
           'album' :album,
           'name': '0',
           'title': '0',
           'description': '0',
           }
    image = client.upload_from_path(PATH, config = config, anon=False)
    return image['link']

def finalize_user_order(f_order_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"UPDATE user_order_confirmed set is_user_confirmed = 1, is_received = 0 where f_order_id = {f_order_id};"
    mycursor.execute(query)
    mydb.commit()

def update_purchase_history(purchase_history):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"insert into purchase_history(purchase_history_id, transaction_id, user_id, quantity_received, plant_status, feedback)values({purchase_history.id}, {purchase_history.transaction_id}, {purchase_history.user_id}, '', '', '{purchase_history.feedback}')"
    mycursor.execute(query)
    mydb.commit()


def pm_refund_save():
    pm_details = payment_method_for_refund.objects.last()
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"INSERT INTO payment_methods_for_refund(pmfr_id, purchase_history_id,payment_method, account_number, account_name) values({pm_details.id},{pm_details.purchase_history_id},'{pm_details.payment_method}','{pm_details.account_num}','{pm_details.account_name}');"
    mycursor.execute(query)
    mydb.commit()

def pm_refund_save_order():
    pm_details = payment_method_for_refund.objects.last()
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"INSERT INTO payment_methods_for_refund(pmfr_id, f_order_id_for_refund ,payment_method, account_number, account_name) values({pm_details.id},{pm_details.purchase_history_id},'{pm_details.payment_method}','{pm_details.account_num}','{pm_details.account_name}');"
    mycursor.execute(query)
    mydb.commit()


def update_pm_refund(purchase_history_id):
    refund_id = req_refund.objects.last()
   
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f'UPDATE payment_methods_for_refund set refund_id = {refund_id.id} where purchase_history_id = {purchase_history_id};'
    mycursor.execute(query)
    mydb.commit()

def is_over(refund_quan,quantity_received,quan_limit):
    if float(quan_limit) < float(quantity_received):
        return True
    elif float(refund_quan) > float(quan_limit):
        return True
    elif float(refund_quan) > float(quantity_received):
        return True
    else:
        return False

def get_quan_limit(data):
    for things in data:
        quan_limit = things['quantity']
    return quan_limit


def save_confirm():
    data = user_order_confirmed.objects.last()
    date = str(datetime.now().date())

    quan = data.confirmed_quantity
    u_order_id = data.u_order_id
    
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"insert into user_order_confirmed(f_order_id,u_order_id,harvest_id,confirmed_quantity,units,total_amount,total_downpayment,dp_due,dp_status,fullpayment_status,is_user_confirmed,is_cancelled,cancel_reason,expected_date_arrival,cancel_date,dp_paid,fp_paid,balance_to_pay,delivery_fee,confirmed_date) values({data.id},{data.u_order_id},{data.harvest_id},'{data.confirmed_quantity}','{data.units}','{data.total_amount}','{data.total_downpayment}','{data.dp_due}','{data.dp_status}','{data.fullpayment_status}','{data.is_user_confirmed}','{data.is_cancelled}','{data.cancel_reason}','{data.expected_date_arrival}','{data.cancel_date}','{data.dp_paid}','{data.fp_paid}','{data.balance_to_pay}','{data.delivery_fee}','{date}')"
    mycursor.execute(query)
    mydb.commit()
    make_refund_info(data.id,data.expected_date_arrival,date)
    reflect_quantity(quan, u_order_id)
    admin_approve(data.u_order_id)


def make_refund_info(f_order_id,expected_date, date):
    ff_order_id = f_order_id
    

    expected_date = datetime.strptime(expected_date, "%Y-%m-%d")
    date = datetime.strptime(date, "%Y-%m-%d")

    gap = expected_date - date
    if gap.days >= 15:
        create = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = date.strftime('%Y-%m-%d'),
        date_to = (date + timedelta(days=1)).strftime('%Y-%m-%d'),
        refund_percentage = "100 %",
        )

        create2 = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = (date + timedelta(days=2)).strftime('%Y-%m-%d'),
        date_to = (date + timedelta(days=5)).strftime('%Y-%m-%d'),
        refund_percentage = "75 %",
        )

        create3 = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = (date + timedelta(days=6)).strftime('%Y-%m-%d'),
        date_to = (date + timedelta(days=8)).strftime('%Y-%m-%d'),
        refund_percentage = "50 %",
        )

        create4 = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = (date + timedelta(days=9)).strftime('%Y-%m-%d'),
        date_to = (date + timedelta(days=11)).strftime('%Y-%m-%d'),
        refund_percentage = "25 %",
        )

        create5 = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = (date + timedelta(days=12)).strftime('%Y-%m-%d'),
        date_to = expected_date.strftime('%Y-%m-%d'),
        refund_percentage = "0 %",
        )
        reflect_to_db_rf_info(ff_order_id)

    elif gap.days == 7:
        create = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = date.strftime('%Y-%m-%d'),
        date_to = date.strftime('%Y-%m-%d'),
        refund_percentage = "50 %",
        )

        create2 = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = (date + timedelta(days=1)).strftime('%Y-%m-%d'),
        date_to = (date + timedelta(days=3)).strftime('%Y-%m-%d'),
        refund_percentage = "25 %",
        )

        create3 = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = (date + timedelta(days=4)).strftime('%Y-%m-%d'),
        date_to = expected_date.strftime('%Y-%m-%d'),
        refund_percentage = "0 %",
        )
        reflect_to_db_rf_info(ff_order_id)

    elif gap.days > 7 <= 14:
        create = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = date.strftime('%Y-%m-%d'),
        date_to = date.strftime('%Y-%m-%d'),
        refund_percentage = "75 %",
        )

        create2 = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = (date + timedelta(days=1)).strftime('%Y-%m-%d'),
        date_to = (date + timedelta(days=3)).strftime('%Y-%m-%d'),
        refund_percentage = "50 %",
        )

        create4 = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = (date + timedelta(days=4)).strftime('%Y-%m-%d'),
        date_to = (date + timedelta(days=6)).strftime('%Y-%m-%d'),
        refund_percentage = "25 %",
        )

        create3 = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = (date + timedelta(days=7)).strftime('%Y-%m-%d'),
        date_to = expected_date.strftime('%Y-%m-%d'),
        refund_percentage = "0 %",
        )
        reflect_to_db_rf_info(ff_order_id)

    elif gap.days == 5 or gap.days == 6:
        create3 = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = date.strftime('%Y-%m-%d'),
        date_to = date.strftime('%Y-%m-%d'),
        refund_percentage = "20 %",
        )

        create3 = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = (date + timedelta(days=1)).strftime('%Y-%m-%d'),
        date_to = expected_date.strftime('%Y-%m-%d'),
        refund_percentage = "0 %",
        )
        reflect_to_db_rf_info(ff_order_id)
    elif gap.days <= 4:
        create3 = refund_info.objects.create(
        f_order_id = ff_order_id,
        date_from = date.strftime('%Y-%m-%d'),
        date_to = expected_date.strftime('%Y-%m-%d'),
        refund_percentage = "0 %",
        )
        reflect_to_db_rf_info(ff_order_id)



def reflect_to_db_rf_info(ff_order_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)

    data = refund_info.objects.filter(f_order_id = ff_order_id)

    for things in data:
        query = f"insert into refund_details values({things.f_order_id},'{things.date_from}','{things.date_to}','{things.refund_percentage}',{things.id});"
        mycursor.execute(query)
        mydb.commit()
        mycursor.close() 
        mycursor = mydb.cursor(dictionary=True) 

def reflect_quantity(quan, u_order_id):
    data = fetch_data(f'select * from user_order_request where u_order_id = {u_order_id}')
    for things in data:
        quan_id = things['quantity_variations_id']
    quan_data = fetch_data(f'select * from batch_quantity_variations where quantity_id = {quan_id}')
    for i in quan_data:
        original_quan = i['quantity_harvested']
    new_quan = float(original_quan) - float(quan) 

    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"update batch_quantity_variations set quantity_harvested = '{new_quan}' where quantity_id = {quan_id};"
    mycursor.execute(query)
    mydb.commit()




def admin_approve(u_order_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"update user_order_request set is_admin_approved = 1 where u_order_id = {u_order_id}"
    mycursor.execute(query)
    mydb.commit()

def save_refund():
    data = refund_info.objects.last()
    sign= " %"
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"insert into refund_details(f_order_id, date_from, date_to, refund_percentage) values({data.f_order_id},'{data.date_from}','{data.date_to}','{str(data.refund_percentage)+sign}')"
    mycursor.execute(query)
    mydb.commit()


def save_delivery_info(shipping_address, contact_info, customer_name):
    data = delivery_info_details.objects.last()
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"insert into delivery_info(transaction_id, f_order_id, delivery_status, details, date_arrived, shipping_address, contact_info, customer_name) values({data.id}, {data.f_order_id},'{data.delivery_status}','{data.details}','{data.date_arrived}', '{shipping_address}', '{contact_info}', '{customer_name}')"
    mycursor.execute(query)
    mydb.commit()

def update_delivery_info(new_delivery_status,new_date_arrived,f_order_id,new_details):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"update delivery_info set delivery_status = '{new_delivery_status}', details='{new_details}', date_arrived='{new_date_arrived}' where f_order_id = {f_order_id}"
    mycursor.execute(query)
    mydb.commit()

    if new_date_arrived != "N/A":
        query2 = f"update user_order_confirmed set is_received = 1 where f_order_id = {f_order_id}"
        mycursor.execute(query2)
        mydb.commit()

def decline_request_db(reason, refund_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"update refund set is_accepted = 3, reason_decline = '{reason}' where refund_id = {refund_id}"
    mycursor.execute(query)
    mydb.commit()

def decline_order(decline_reason, u_order_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f'update user_order_request set is_admin_approved = 2, request_decline_reason = "{decline_reason}" where u_order_id = {u_order_id}'
    mycursor.execute(query)
    mydb.commit()
    send_decline_message(u_order_id, decline_reason)


def decline_redelivery_db(reason, re_delivery_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f'update re_delivery set is_accepted = 3, reason_decline = "{reason}" where re_delivery_id = {re_delivery_id};'
    mycursor.execute(query)
    mydb.commit()



def accept_refund(refund_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"update refund set is_accepted = 1 where refund_id = {refund_id}"
    mycursor.execute(query)
    mydb.commit()

def accept_redelivery(re_delivery_id):
    date = str(datetime.now().date())
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"update re_delivery set is_accepted = 1, redelivery_request_date_accepted = '{date}' where re_delivery_id = {re_delivery_id}"
    mycursor.execute(query)
    mydb.commit()

def save_pm(pm_id, f_order_id):
    data = payment_methods.objects.get(id = pm_id)
    create = payment_methods.objects.create(
                payment_method = data.payment_method,
                f_order_id = f_order_id,
                account_name = data.account_name,
                account_number = data.account_number,
                )

    data = payment_methods.objects.last()
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"insert into payment_methods(p_id,f_order_id,payment_method,account_number,account_name) values({data.id},{f_order_id},'{data.payment_method}','{data.account_number}','{data.account_name}')"
    mycursor.execute(query)
    mydb.commit()




def update_pmEdit(dic, p_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"update payment_methods set is_confirmed = 1, payment_method = '{dic['new_payment_method']}', account_number = '{dic['new_account_number']}', account_name = '{dic['new_account_name']}',amount_paid = '{dic['new_amount_paid']}', payment_for = '{dic['new_payment_for']}' where p_id = {p_id};"
    mycursor.execute(query)
    mydb.commit()

def update_pm(dic, p_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"update payment_methods set payment_method = '{dic['new_payment_method']}', account_number = '{dic['new_account_number']}', account_name = '{dic['new_account_name']}' where p_id = {p_id};"
    mycursor.execute(query)
    mydb.commit()

def update_refund_details(new_dateto,new_datefrom,new_percentage,rd_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"update refund_details set date_from = '{new_datefrom}', date_to = '{new_dateto}', refund_percentage = '{new_percentage}' where rd_id = {rd_id};"
    mycursor.execute(query)
    mydb.commit()

def get_harvest_id(re_delivery_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"select * from re_delivery inner join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join batch_harvest on user_order_request.harvest_id = batch_harvest.harvest_id where re_delivery.re_delivery_id = {re_delivery_id};"
    mycursor.execute(query)
    data = mycursor.fetchall()
    harvest_id = ""
    for things in data:
        harvest_id = things['harvest_id']
    return harvest_id

def refund_pay(pmfr_id,refund_id):
    data = confirm_refund.objects.last()
    link = get_img_link(data.proof_of_refund)
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"update payment_methods_for_refund set proof_receipt = '{link}', is_selected = 1 where pmfr_id = {pmfr_id};"
    query2 = f"update refund set date_of_refund ='{data.date_of_refund}', refund_amount ='{data.refund_amount}', refund_status ='{data.refund_status}' where refund_id = {refund_id}"
    mycursor.execute(query)
    mydb.commit()

    mycursor.execute(query2)
    mydb.commit()

def refund_pay_order(pmfr_id,f_order_id):
    data = confirm_refund.objects.last()
    link = get_img_link(data.proof_of_refund)
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"update payment_methods_for_refund set proof_receipt = '{link}', is_selected = 1 where pmfr_id = {pmfr_id};"
    query2 = f"update user_order_confirmed set refund_date ='{data.date_of_refund}' where f_order_id = {f_order_id}"
    mycursor.execute(query)
    mydb.commit()

    mycursor.execute(query2)
    mydb.commit()


def confirm__redelivery_details(re_delivery_id):
    data = model_redelivery_details.objects.last()

    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"insert into redelivery_info(re_delivery_id, quantity_variations_id, harvest_id, quantity_delivered) values('{re_delivery_id}','{data.quantity_variations_id}','{data.harvest_id}','{data.quantity_delivered}')"
    mycursor.execute(query)
    mydb.commit()

def add_db_redelivery_info(re_delivery_id, shipping_address,contact_info, customer_name):
    data = redelivery_info_update.objects.last()
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True) 
    query=f"UPDATE redelivery_info set contact_info = '{contact_info}', customer_name= '{customer_name}', re_delivery_status ='{data.re_delivery_status}',details ='{data.details}',date_arrived ='{data.date_arrived}',date_shipped ='{data.date_shipped}',expected_arrival ='{data.expected_arrival}',shipping_address ='{shipping_address}'  where re_delivery_id = {re_delivery_id}"
    mycursor.execute(query)
    mydb.commit()
    new_data = fetch_data(f'select * from redelivery_info where re_delivery_id = {re_delivery_id};')
    for new in new_data:
        status = new['re_delivery_status']
    query3 =f"update re_delivery set redelivery_status = '{status}' where re_delivery_id = {re_delivery_id};"
    mycursor.execute(query3)
    mydb.commit()
    
def update_db_redelivery_info(request, re_delivery_id):
    rd_status = request.POST['re_delivery_status']
    details = request.POST['details']
    if request.POST['date_arrived'] == "":
        d_a = "N/A"
    else:
        d_a = request.POST['date_arrived']

    if request.POST['date_shipped'] == "":
        d_s = "N/A"
    else:
        d_s = request.POST['date_shipped']

    if request.POST['expected_arrival'] == "":
        e_a = "N/A"
    else:
        e_a = request.POST['expected_arrival']


    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"UPDATE redelivery_info set re_delivery_status ='{rd_status}',details ='{details}',date_arrived ='{d_a}',date_shipped ='{d_s}',expected_arrival ='{e_a}'  where re_delivery_id = {re_delivery_id}"
    mycursor.execute(query)
    mydb.commit()
    new_data = fetch_data(f'select * from redelivery_info where re_delivery_id = {re_delivery_id};')
    for new in new_data:
        status = new['re_delivery_status']
    query3 =f"update re_delivery set redelivery_status = '{status}' where re_delivery_id = {re_delivery_id};"
    mycursor.execute(query3)
    mydb.commit()


def check_dateRefund(date_from,date_to,percentage, f_order_id, rd_id):
    messages = []
    date_today = datetime.strptime(datetime.today().strftime('%Y-%m-%d'), "%Y-%m-%d")
    date1 = datetime.strptime(date_from, "%Y-%m-%d")
    date2 = datetime.strptime(date_to, "%Y-%m-%d")
    all_dates = fetch_data(f"select * from refund_details where f_order_id = {f_order_id} and rd_id in(select rd_id from refund_details where rd_id !={rd_id})")
    if date1 > date2:
         return False, "Date_from must not exceed Date_to input"
    elif date_today > date1:
        return False, 'Inputted Date_From Date has already passed'
    elif date_today > date2:
        return False, 'Inputted Date_to Date has already passed'
    else:
        for i in all_dates:
            if datetime.strptime(str(i['date_from']), "%Y-%m-%d") <= date1 <= datetime.strptime(str(i['date_to']), "%Y-%m-%d"):
                return False, "Date has conflict with other dates Please check the Refund table for basis"
            elif datetime.strptime(str(i['date_from']), "%Y-%m-%d") <= date2 <= datetime.strptime(str(i['date_to']), "%Y-%m-%d"):
                return False, "Date has conflict with other dates Please check the Refund table for basis"
            elif percentage == i['refund_percentage']:
                return False, 'Refund Percentage already exists in the Table'
                

    return True, "Refund details Updated"

def cancel_if_not_paid(u_order_id):
    a = False
    date_today = datetime.strptime(str(datetime.now().date()),'%Y-%m-%d')
    data = fetch_data(f'select * from user_order_confirmed where u_order_id = {u_order_id};')
    for things in data:
        dp_due = datetime.strptime(things['dp_due'], '%Y-%m-%d')    
    if dp_due < date_today:
        a = cancel_order_dp_not_paid(u_order_id)
        return_quantity(u_order_id)
        return a
    return False



def return_quantity(u_order_id):
    data = fetch_data(f'select * from user_order_confirmed where u_order_id = {u_order_id};')
    data2 = fetch_data(f'select * from batch_quantity_variations inner join user_order_request on batch_quantity_variations.quantity_id = user_order_request.quantity_variations_id where user_order_request.u_order_id = {u_order_id};')
    
    for i in data:
        confirmed_quantity = i['confirmed_quantity']
    for ii in data2:
        old_quantity = ii['quantity_harvested']
        quantity_id = ii['quantity_variations_id']

    new_quantity = float(confirmed_quantity) + float(old_quantity)
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"update batch_quantity_variations set quantity_harvested = '{new_quantity}' where quantity_id = {quantity_id};"
    mycursor.execute(query)
    mydb.commit()


def cancel_order_dp_not_paid(u_order_id):
    date_today = str(datetime.now().date())
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    data = fetch_data(f'select * from user_order_confirmed where u_order_id = {u_order_id}')
    for datas in data:
        if datas['dp_paid'] != "1":
            query=f"UPDATE user_order_confirmed set is_cancelled = 1, cancel_reason='User failed to pay the Down Payment on its Due date', cancel_date='{date_today}', cancel_refund_amount ='0', refund_date='{date_today}' where u_order_id = {u_order_id} "
            mycursor.execute(query)
            mydb.commit()
            return True
    return False

def update_quantity(quan_id,quan_delivered):
    quan_id = int(quan_id)
    quan_delivered = float(quan_delivered)
    data = fetch_data(f'select * from batch_quantity_variations where quantity_id = {quan_id}')
    for i in data:
        curr_quan = float(i['quantity_harvested'])
    new_quan = curr_quan - quan_delivered
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"UPDATE batch_quantity_variations set quantity_harvested = {new_quan} where quantity_id = {quan_id} "
    mycursor.execute(query)
    mydb.commit()

def add_announcement_db():
    date_today = str(datetime.now().date())
    data = announcement.objects.last()
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"insert into announcements(a_id, a_title, a_desc, a_link, a_days, a_date_published) values({data.id},'{data.a_title}','{data.a_desc}','{data.a_link}','{data.a_days}','{date_today}');"
    mycursor.execute(query)
    mydb.commit()

def update_announcement_db(request, a_id):
    date_today = str(datetime.now().date())
    data = announcement.objects.last()
    a_title =request.POST['a_title']
    a_link =request.POST['a_link']
    a_days =request.POST['a_days']
    a_desc =request.POST['a_desc']
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f'update announcements set a_title ="{a_title}", a_desc ="{a_desc}", a_link ="{a_link}", a_days ="{a_days}"  where a_id = {a_id}'
    mycursor.execute(query)
    mydb.commit()

def check_announcement_date_remaning():
    date_today = datetime.now().date()
    mydb = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="root",
    database="farmsys",
    )
    mycursor = mydb.cursor(dictionary=True)
    data = fetch_data('select * from announcements where a_status = 1')

    for things in data:
        date_published = datetime.strptime(things['a_date_published'], '%Y-%m-%d').date()
        days = float(things['a_days'])
        dd = date_today - date_published 
        a_id = things['a_id']
        if dd.days >= days:
            query=f"UPDATE announcements set a_status = {0} where a_id = {a_id};"
            mycursor.execute(query)
            mydb.commit()


def set_refund_paid(f_order_id):
    date_today = datetime.now().date()
    mydb = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="root",
    database="farmsys",
    )
    mycursor = mydb.cursor(dictionary=True)
    query=f"UPDATE user_order_confirmed set refund_date = '{date_today}' where f_order_id = {f_order_id};"
    mycursor.execute(query)
    mydb.commit()
            

def update_profile_info(request):
    user_id = get_user_id(request.user.username)
    

    mydb = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="root",
    database="farmsys",
    )
    mycursor = mydb.cursor(dictionary=True)
    query=f"UPDATE user_acc set phone_num = '{request.POST['phone_num']}', email_ad = '{request.POST['email_ad']}', full_name = '{request.POST['full_name']}', company = '{request.POST['company']}', socials = '{request.POST['socials']}'  where user_id = {user_id};"
    mycursor.execute(query)
    mydb.commit()
    query2=f"UPDATE address set barangay = '{request.POST['barangay']}', block = '{request.POST['block']}', lot = '{request.POST['lot']}', street = '{request.POST['street']}', city = '{request.POST['city']}', province = '{request.POST['province']}', zipcode = '{request.POST['zipcode']}' where user_id = {user_id};"
    mycursor.execute(query2)
    mydb.commit()

def updpate_shipping_address(request):
    user_id = get_user_id(request.user.username)
    new_address = request.POST['shipping_address']
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"UPDATE user_acc set shipping_address = '{new_address}' where user_id = {user_id};"
    mycursor.execute(query)
    mydb.commit()
    user = User.objects.get(username=request.user.username)
    user.last_name = new_address
    user.save()

def set_sh_address_default(request, address_id):
    user_id = get_user_id(request.user.username)
    data = fetch_data(f'select * from address where address_id = {address_id}')
    new_address = ""
    for i in data:
        new_address = f"{i['block']}, {i['lot']}, {i['street']}, {i['barangay']}, {i['city']}, {i['province']}, {i['zipcode']}"
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query = f"UPDATE user_acc set shipping_address = '{new_address}' where user_id = {user_id};"
    mycursor.execute(query)
    mydb.commit()
    user = User.objects.get(username=request.user.username)
    user.last_name = new_address
    user.save()


    messages.error(request, "Shipping Address Successfully Updated")
    return redirect('profile')

def changepassword_db(request):

    user_id = get_user_id(request.user.username)
    data = fetch_data(f'select * from user_acc where user_id ={user_id}')
    is_ok = False
    for i in data:
        if i['main_pass']:
            is_ok = True
    new_pass = request.POST['new_pass']
    og_pass = request.POST['old_pass']
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    if is_ok == True:
        query = f"UPDATE user_acc set pass = '{new_pass}'  where user_id = {user_id};"
    else:
        query = f"UPDATE user_acc set pass = '{new_pass}', main_pass='{og_pass}'  where user_id = {user_id};"
    mycursor.execute(query)
    mydb.commit()

def check_if_user_exists(username, password):
    accounts = fetch_data("select * from user_acc")
    
    for i in accounts:
        if i['username'] == username and i['pass'] == password:
            if i['main_pass']:
                return i['username'], i['main_pass'], True
            else:
                return i['username'], i['pass'], True
    return username,password, False

def get_shipping_address(f_order_id):
    data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where user_order_confirmed.f_order_id = {f_order_id}')
    for i in data:
        if i['shipping_address']:
            return i['shipping_address'], i['phone_num'], i['full_name']
        else:
            data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id inner join address on user_acc.user_id = address.user_id where user_order_confirmed.f_order_id = {f_order_id};')
            for ii in data:
                return f"{ii['block']}, {ii['lot']}, {ii['street']}, {ii['barangay']}, {ii['city']}, {ii['province']}, {ii['zipcode']}", i['phone_num'], i['full_name']

def get_shipping_address2(re_delivery_id):
    data = fetch_data(f'select * from re_delivery inner join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where re_delivery.re_delivery_id = {re_delivery_id}')
    

    for i in data:
        if i['shipping_address']:
            return i['shipping_address'], i['phone_num'], i['full_name']
        else:
            data = fetch_data(f'select * from re_delivery inner join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id inner join address on user_acc.user_id = address.user_id where re_delivery.re_delivery_id = {re_delivery_id}')
            for ii in data:
                return f"{ii['block']}, {ii['lot']}, {ii['street']}, {ii['barangay']}, {ii['city']}, {ii['province']}, {ii['zipcode']}", i['phone_num'], i['full_name']

def save_address(user_id):
    address_data = address.objects.last()
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"insert into address(user_id, lot,street,city,province,zipcode, block, barangay) values({user_id},'{address_data.lot}','{address_data.street}','{address_data.city}','{address_data.province}','{address_data.zipcode}','{address_data.block}','{address_data.barangay}');"
    mycursor.execute(query)
    mydb.commit()

def check_is_admin_exists(username, password):
    admin_accounts = fetch_data("select * from employee_accounts")
    for ii in admin_accounts:
        if username == ii['username'] and password == ii['pass']:
            return True
    return False



def check_user_already_exists(username):
    accounts = fetch_data("select * from user_acc")
    for ii in accounts:
        if username == ii['username']:
            return True

    return False

def filter_order_requests(query, order_by):
    if order_by == "full_name":
        data = fetch_data(f"{query} order by user_acc.{order_by}")
        return data
    else:
        if order_by == "u_order_id":
            data = fetch_data(f"{query} order by user_order_request.{order_by} desc")
            return data

        else:
            if order_by == "order_request_date":
                data = fetch_data(f"{query} order by user_order_request.{order_by} desc")
                return data
            else:
                data = fetch_data(f"{query} order by user_order_request.{order_by}")
                return data

def filter_admin_redelivery(order_by):
    if order_by in ["redelivery_status","is_accepted","request_date"]:
        if order_by == "request_date":
            data =fetch_data(f'select * from re_delivery left join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id left join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id left join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select redelivery_info.re_delivery_id as rdo_ready,redelivery_info.re_delivery_status as rdi_ready from redelivery_info left join re_delivery on redelivery_info.re_delivery_id = re_delivery.re_delivery_id) as rd_ready on rd_ready.rdo_ready = re_delivery.re_delivery_id order by re_delivery.{order_by} desc')
        else:
            data =fetch_data(f'select * from re_delivery left join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id left join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id left join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select redelivery_info.re_delivery_id as rdo_ready,redelivery_info.re_delivery_status as rdi_ready from redelivery_info left join re_delivery on redelivery_info.re_delivery_id = re_delivery.re_delivery_id) as rd_ready on rd_ready.rdo_ready = re_delivery.re_delivery_id order by re_delivery.{order_by}')

    else:
        if order_by == "full_name":
            data =fetch_data(f'select * from re_delivery left join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id left join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id left join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select redelivery_info.re_delivery_id as rdo_ready,redelivery_info.re_delivery_status as rdi_ready from redelivery_info left join re_delivery on redelivery_info.re_delivery_id = re_delivery.re_delivery_id) as rd_ready on rd_ready.rdo_ready = re_delivery.re_delivery_id order by user_acc.{order_by}')
        elif order_by == 'u_order_id':
            data =fetch_data(f'select * from re_delivery left join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id left join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id left join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select redelivery_info.re_delivery_id as rdo_ready,redelivery_info.re_delivery_status as rdi_ready from redelivery_info left join re_delivery on redelivery_info.re_delivery_id = re_delivery.re_delivery_id) as rd_ready on rd_ready.rdo_ready = re_delivery.re_delivery_id order by user_order_request.{order_by} desc')
        else:
            data =fetch_data(f'select * from re_delivery left join purchase_history on re_delivery.purchase_history_id = purchase_history.purchase_history_id left join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id left join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id left join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id left join user_acc on user_order_request.user_id = user_acc.user_id left join (select redelivery_info.re_delivery_id as rdo_ready,redelivery_info.re_delivery_status as rdi_ready from redelivery_info left join re_delivery on redelivery_info.re_delivery_id = re_delivery.re_delivery_id) as rd_ready on rd_ready.rdo_ready = re_delivery.re_delivery_id order by user_order_request.{order_by}')
    return data

def filter_admin_cancelled(order_by):
    if order_by == "full_name":
        data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id  where is_cancelled = 1 order by user_acc.{order_by};')
    elif order_by == "u_order_id":
        data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id  where is_cancelled = 1 order by user_order_request.{order_by} desc; ')
    elif order_by == "plant_name":
        data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id  where is_cancelled = 1 order by user_order_request.{order_by};')
    elif order_by == "refund_date":
        data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id  where is_cancelled = 1 order by user_order_confirmed.{order_by};')
    elif order_by == "cancel_date":
        data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id  where is_cancelled = 1 order by user_order_confirmed.{order_by} desc;')
    return data

def filter_admin_refund(order_by):
    if order_by == "full_name":
        data = fetch_data(f"select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.remove_to_view = 0 order by user_acc.{order_by}")
    elif order_by in ['request_date','is_accepted','refund_amount']:
        if order_by == "request_date":
            data = fetch_data(f"select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.remove_to_view = 0 order by refund.{order_by} desc")
        else:
            data = fetch_data(f"select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.remove_to_view = 0 order by refund.{order_by}")
    else:
        if order_by == "u_order_id":
            data = fetch_data(f"select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.remove_to_view = 0 order by user_order_request.{order_by} desc")
        else:    
            data = fetch_data(f"select * from refund inner join purchase_history on refund.purchase_history_id = purchase_history.purchase_history_id inner join delivery_info on purchase_history.transaction_id = delivery_info.transaction_id inner join user_order_confirmed on delivery_info.f_order_id = user_order_confirmed.f_order_id inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id where refund.remove_to_view = 0 order by user_order_request.{order_by}")
    return data 

def filter_received_orders(order_by):
    if order_by in ['plant_name',"u_order_id"]:
        if order_by == "u_order_id":
            data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id where user_order_confirmed.is_received = 1 and payment_methods.is_selected = 1 order by user_order_request.{order_by} desc')
        else:
            data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id where user_order_confirmed.is_received = 1 and payment_methods.is_selected = 1 order by user_order_request.{order_by}')
    elif order_by == "full_name":
        data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id where user_order_confirmed.is_received = 1 and payment_methods.is_selected = 1 order by user_acc.{order_by}')
    elif order_by == "payment_method":
        data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id where user_order_confirmed.is_received = 1 and payment_methods.is_selected = 1 order by payment_methods.{order_by}')
    elif order_by == "date_arrived":
        data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id where user_order_confirmed.is_received = 1 and payment_methods.is_selected = 1 order by delivery_info.{order_by} desc')
    elif order_by == "total_amount_paid":
        data = fetch_data(f'select * from user_order_confirmed inner join user_order_request on user_order_confirmed.u_order_id = user_order_request.u_order_id inner join user_acc on user_order_request.user_id = user_acc.user_id inner join delivery_info on user_order_confirmed.f_order_id = delivery_info.f_order_id inner join payment_methods on user_order_confirmed.f_order_id = payment_methods.f_order_id where user_order_confirmed.is_received = 1 and payment_methods.is_selected = 1 order by payment_methods.{order_by} desc')
    return data

def filter_announcements(order_by):
    if order_by in ["a_date_published" , "a_days","a_status"]:
        data = fetch_data(f'select * from announcements order by {order_by} desc;')
    else:
        data = fetch_data(f'select * from announcements order by {order_by};')
    return data

def set_to_sold_out(harvest_id):
    data = fetch_data(f'select * from batch_harvest inner join batch_quantity_variations on batch_harvest.harvest_id = batch_quantity_variations.harvest_id where batch_harvest.harvest_id = {harvest_id}')
    total_quan_left = 0
    for ii in data:
        total_quan_left = total_quan_left + float(ii['quantity_harvested'])
    if total_quan_left <= 0:
        mydb = mysql.connector.connect(
        host ="localhost",
        user="root",
        password="root",
        database="farmsys",
        )
        mycursor = mydb.cursor(dictionary=True)
        query=f"update batch_harvest set batch_status = 'Sold Out' where harvest_id = {harvest_id}"
        mycursor.execute(query)
        mydb.commit()
        return True

def update_pma_db():
    datas = payment_methods.objects.filter(for_admin = 1)
    mydb = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="root",
    database="farmsys",
    )
    mycursor = mydb.cursor(dictionary=True)
    for data in datas:
        query = f"Insert ignore into payment_methods_admin(pma_id, payment_method, account_number, account_name) values({data.id}, '{data.payment_method}', '{data.account_number}', '{data.account_name}')"
        mycursor.execute(query)
        mydb.commit()
        mycursor.close() 
        mycursor = mydb.cursor(dictionary=True) 


def set_quantity_to_inactive():
    datas = fetch_data(f"select * from batch_quantity_variations where var_status = 'Active' ")

    mydb = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="root",
    database="farmsys",
    )
    mycursor = mydb.cursor(dictionary=True)
    for data in datas:
        if float(data['quantity_harvested'] ) <= 0:
            query = f"update batch_quantity_variations set var_status ='Inactive' where quantity_id = {data['quantity_id']};"
            mycursor.execute(query)
            mydb.commit()
            mycursor.close() 
            mycursor = mydb.cursor(dictionary=True) 

def send_email_order_confirmation(u_order_id):
    user_id = "0"
    data = fetch_data(f'select * from user_order_request where u_order_id = {u_order_id}')
    farm_data = fetch_data(f'select * from farm')
    
    for ii in farm_data:
        farmname = ii['farm_name']
    for things in data:
        user_id = things['user_id']
        data = fetch_data(f'select * from user_acc where user_id = {user_id}')
        for things2 in data:
            email = things2['email_ad']
            name = things2['full_name']
    code = f'Good day {name}!,\n\nThank you for ordering from {farmname}.\nYour order # ({u_order_id}) has been confirmed.\nYou can review your order details at any time by visiting our Website ^^.\n\nThank you for sending your Request!'
    email = EmailMessage(
        'Order Confirmation',#subject
        code,#message
        'jarheetalo@gmail.com',#from
        [email],) #to
    email.fail_silenty=False
    email.send()
    #FROM MY TWILIO ACCOUNT
    account_sid = "AC64b6d23ab97b6adedd0fd11465fcd59c"
    auth_token = "9974f805ffcde70bf0ebee6c7654f510"
    client = Client(account_sid, auth_token)
    #message = client.messages('MM800f449d0399ed014aae2bcc0cc2f2ec').fetch()
    message = client.messages.create(body=f'\n{code}',from_= "+12292972135",to="+639939580551")



def send_decline_message(u_order_id, reason):
    user_id = "0"
    data = fetch_data(f'select * from user_order_request where u_order_id = {u_order_id}')
    farm_data = fetch_data(f'select * from farm')
    
    for ii in farm_data:
        farmname = ii['farm_name']
    for things in data:
        user_id = things['user_id']
        data = fetch_data(f'select * from user_acc where user_id = {user_id}')
        for things2 in data:
            email = things2['email_ad']
            name = things2['full_name']
    code = f'Good day {name}!,\n\nThank you for ordering from {farmname}.\nWe are sorry, but your order #({u_order_id}) has been declined.\nThe reason is: ({reason}).\n\nThank you for sending your Request!'
    email = EmailMessage(
        'Order Confirmation',#subject
        code,#message
        'jarheetalo@gmail.com',#from
        [email],) #to
    email.fail_silenty=False
    email.send()
    #FROM MY TWILIO ACCOUNT
    account_sid = "AC64b6d23ab97b6adedd0fd11465fcd59c"
    auth_token = "9974f805ffcde70bf0ebee6c7654f510"
    client = Client(account_sid, auth_token)
    #message = client.messages('MM800f449d0399ed014aae2bcc0cc2f2ec').fetch()
    message = client.messages.create(body=f'\n{code}',from_= "+12292972135",to="+639939580551")

def upload_to_imgur():
    data = fetch_data("select * from batch_harvest")
    for things in data:
        if things['batch_img_imgur']:
            pass
        else:
            if things['batch_img'].lower().startswith("http"):
                reflect_image(things['batch_img'], things['harvest_id'])
            else:
                image_link = upload_image(things['batch_img'])
                reflect_image(image_link, things['harvest_id'])

def upload_image(code):
    image = base64.b64decode(str(code)+ "==")
    img_file = open('image.jpeg', 'wb')
    img_file.write(image)
    img_file.close()

    directory = 'image.jpeg'

    CLIENT_ID = '851c881d15a628e'
    CLIENT_SECRET = 'de18eba31b31c91cc3134f1bea74c39b80e099ed'
    imgr_username = "rheejan"   
    imgr_password = "09491751465"

    client = ImgurClient(CLIENT_ID, CLIENT_SECRET)

    auth_url = client.get_auth_url('pin')

    #PATH =f'../images/{receipt}'
    PATH = f'image.jpeg' 
    album=  None

    config={
           'album' :album,
           'name': '0',
           'title': '0',
           'description': '0',
           }
    image = client.upload_from_path(PATH, config = config, anon=False)
    return image['link']

def reflect_image(link, harvest_id):
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    query=f"UPDATE batch_harvest set batch_img_imgur = '{link}' where harvest_id = {harvest_id}"
    mycursor.execute(query)
    mydb.commit()


def upload_imgur_image():
    yes = False
    link =""
    s_id = ""
    mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="root",
       database="farmsys",
       )
    mycursor = mydb.cursor(dictionary=True)
    data = fetch_data('select * from social_info')
    for things in data:
        if things['org_chart_imgur']:
            pass
            yes = True
        else:
            link = upload_image(things['org_chart'])
            s_id = things['s_id']
            
    if yes == False:
        query=f"UPDATE social_info set org_chart_imgur = '{link}' where s_id = {s_id};"
        mycursor.execute(query)
        mydb.commit()


    
