from django.db import models
import datetime
from datetime import date
from datetime import datetime,timedelta
# Create your models here.

########################################
from django.db import models

class Event(models.Model):
    activities_id = models.IntegerField(null=True, blank=True)
    batch_id = models.IntegerField()
    plant_stage = models.CharField(max_length=2000,null=True, blank=True)
    activity = models.CharField(max_length=2000,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    remarks = models.CharField(max_length=2000,null=True, blank=True)

    def __str__(self):
        return f"Activity Id: {self.activities_id}"
        

class user_account(models.Model):
    username = models.CharField(max_length=200)
    passw = models.CharField(max_length=200)
    confirm_passw = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=200)
    email_ad = models.CharField(max_length=200)
    is_authenticated = models.BooleanField(default=False)
    full_name = models.CharField(max_length=200, null=True)
    comp = models.CharField(max_length=20, blank= True)
    adress = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.username}'

class user_order_request(models.Model):
    user_id = models.IntegerField()
    harvest_id = models.IntegerField()
    plant_name = models.CharField(max_length=200)
    
    quantity_variations_id = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    
    date_needed = models.CharField(max_length=200)
    is_admin_approved = models.BooleanField(default=False,null=True,blank= True)


    def __str__(self):
        return f"{self.user_id} orders {self.plant_name}"




class payments(models.Model):
    #img_proof
    #payment_for
    #payment_method
    p_id = models.IntegerField()
    payment_for = models.CharField(max_length=200)
    proof_receipt = models.ImageField() #null=True,blank= True
    amount_paid = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}"

class purchase_history(models.Model):
    transaction_id = models.IntegerField()
    user_id = models.IntegerField()
    feedback = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}"

class req_redelivery(models.Model):
    transac_id = models.IntegerField() #purchase history ID
    quan_received = models.IntegerField()
    returned_quan = models.IntegerField()
    units = models.CharField(max_length=200)
    reason_rd = models.CharField(max_length=200)
    proof_pic = models.ImageField() 


    def __str__(self):
        return f'{self.id}'

class req_refund(models.Model):
    transac_id = models.IntegerField()
    quantity_received = models.IntegerField()
    refund_quan = models.FloatField()
    units = models.CharField(max_length=200)
    reason_refund = models.CharField(max_length=200)
    proof_refund = models.ImageField() 

    def __str__(self):
        return f'{self.id}'

class payment_method_for_refund(models.Model):
    purchase_history_id = models.IntegerField()
    payment_method = models.CharField(max_length=200)
    payment_for = models.CharField(max_length=200) 
    account_num = models.CharField(max_length=200) 
    account_name = models.CharField(max_length=200)


    def __str__(self):
        return f'{self.id}'

class user_order_confirmed(models.Model):
    u_order_id = models.IntegerField(default=0)
    harvest_id = models.IntegerField(default=0)
    plant_name = models.CharField(max_length=200,default="0")
    confirmed_quantity = models.CharField(max_length=200,default="0")
    units = models.CharField(max_length=200,default="0")
    total_amount = models.CharField(max_length=200,default="0")
    total_downpayment = models.CharField(max_length=200,default="0")
    dp_due = models.CharField(max_length=200,default="0")
    dp_status = models.IntegerField(default=0) 
    fullpayment_status = models.IntegerField(default=0) 
    is_user_confirmed = models.IntegerField(default=0)
    is_cancelled = models.IntegerField(default=0)
    cancel_reason = models.CharField(max_length=200,default="0")
    expected_date_arrival = models.CharField(max_length=200,default="0") 
    cancel_date = models.CharField(max_length=200,default="0")
    dp_paid = models.CharField(max_length=200,default="0")
    fp_paid = models.CharField(max_length=200,default="0")
    balance_to_pay = models.CharField(max_length=200,default="0")
    delivery_fee = models.CharField(max_length=200,default="0")

    def __str__(self):
        return f'{self.id}'


class refund_info(models.Model):
    f_order_id = models.IntegerField()
    date_from = models.CharField(max_length=200) 
    date_to = models.CharField(max_length=200) 
    refund_percentage = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.f_order_id}'


class delivery_info_details(models.Model):
    f_order_id = models.IntegerField()
    delivery_status = models.CharField(max_length=200, default="Ongoing")
    details = models.CharField(max_length=1000)
    date_arrived = models.CharField(max_length=200, default="N/A")

    def __str__(self):
        return f'{self.id}'


class payment_methods(models.Model):
    f_order_id = models.IntegerField(default=0)
    payment_method = models.CharField(max_length=200)
    payment_for = models.CharField(max_length=200,default="0")
    account_number = models.CharField(max_length=200)
    account_name = models.CharField(max_length=200)
    proof_receipt = models.CharField(max_length=200,default="0") 
    is_selected = models.CharField(max_length=200,default="0")
    amount_paid = models.CharField(max_length=200,default="0") 
    date_paid = models.CharField(max_length=200,default="0")
    for_admin = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}'




class confirm_refund(models.Model):
    date = str(datetime.now().date())

    date_of_refund= models.CharField(max_length=200, default=date)
    refund_amount= models.CharField(max_length=200)
    proof_of_refund = models.ImageField()
    refund_status= models.IntegerField(default = 1)

    def __str__(self):
        return f'{self.id}'

class model_redelivery_details(models.Model):

    quantity_delivered = models.IntegerField(default = 0)
    quantity_variations_id = models.IntegerField(default = 0)
    harvest_id = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.id}'


class redelivery_info_update(models.Model):
    re_delivery_status = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    date_arrived = models.CharField(max_length=200, default = "N/A")
    date_shipped = models.CharField(max_length=200, default = "N/A")
    expected_arrival = models.CharField(max_length=200, default = "N/A")

    def __str__(self):
        return f'{self.id}'

class announcement(models.Model):
    a_title = models.CharField(max_length=2000)
    a_link = models.CharField(max_length=2000)
    a_desc = models.CharField(max_length=2000)
    a_days = models.CharField(max_length=2000) 

    def __str__(self):
        return f'{self.a_title}'



class address(models.Model):
    lot = models.CharField(max_length=2000, default= "")
    street = models.CharField(max_length=2000, default= "")
    city = models.CharField(max_length=2000, default= "")
    province = models.CharField(max_length=2000, default= "")
    zipcode = models.CharField(max_length=2000, default= "")
    block = models.CharField(max_length=2000, default= "")
    barangay = models.CharField(max_length=2000, default= "")
    def __str__(self):
        return self.id



########################################
