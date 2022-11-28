from django import template
from datetime import datetime
import base64
from django import template
from django.contrib.staticfiles.finders import find as find_static_file
from django.conf import settings


register = template.Library()


@register.simple_tag
def encode_static(path, encoding='base64', file_type='image'):
    """
    a template tag that returns a encoded string representation of a staticfile
    Usage::
        {% encode_static path [encoding] %}
    Examples::
        <img src="{% encode_static 'path/to/img.png' %}">
    """
    try:
        file_path = find_static_file(path)
        ext = file_path.split('.')[-1]
        file_str = get_file_data(file_path).encode(encoding)
        return u"data:{0}/{1};{2},{3}".format(file_type, ext, encoding, file_str)
    except IOError:
        return ''


def get_file_data(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
        return data


@register.simple_tag
def to_image(code):
    image = base64.b64decode(code)
    path = './images/1.jpeg'
    img_file = open(path, 'wb')
    img_file.write(image)
    img_file.close()
    return path

@register.filter()
def encode(value):
    value = base64.b64encode(str(value))
    value = value.decode()
    return f"data:image/jpeg;base64,' {value} '"

    



@register.filter()
def split(value, key):
    try:
        return value.split(key)
    except:
        return value


@register.filter()
def date_format(value):
    if value == "0":
        return "N/A"
    
    try:
        date = value.split('-')
        m = date[1]
        d = date[2]
        y = date[0]
        fdate = f'{m}/{d}/{y}'
        return fdate
    except:
        return value


@register.filter()
def price_per_unit(quan, tot):
    return "{:.2f}".format(float(tot)/float(quan))

@register.filter()
def calc_soa(a,b):
    if a is None:
        a = 0 
    if b is None:
        b = 0
    return "{:.2f}".format(float(a) - float(b))

@register.filter()
def delivery_format(value):
    a = value.split(';')
    b=""
    for i in a:
        b = b + i + "\n"
    return b

@register.filter()
def money_format(a):
    if a == "" or a == None:
        return a 

    return f'Php. {"{:.2f}".format(float(a))}'

@register.filter()
def quan_format(a):
    if a == "":
        return a 
    else:
        return int(float(a))

@register.filter()
def to_float(value):
    if value =="":
        return value
    else:
        return float(value)

@register.filter()
def to_int(value):
    try:
        return int(value)
    except:
        return value

@register.filter()
def add(value, value2):
    if value == "" or value2 =="":
        return ""
    else:
        return (float(value) + float(value2))

@register.filter()
def status_format(value):
    try:
        value = int(value)
        if value == 1:
            return "Paid"
        elif value == 0:
            return "Not enough Payment"
        else:
            return value
    except:
        return value

@register.filter()
def remove_sign(value):
    try:
        a = value.split(" ")
        return a[0]
    except:
        return value

@register.filter()
def announcement_status(value):
    try:
        if value == 1 or value == "1":
            return "Active"
        else:
            return "Inactive"
    except:
        return value


@register.filter()
def calc_refund_p(r_quan, t_quan):
    return f"{(float(r_quan)/float(t_quan)) * 60}%"



@register.simple_tag
def calc_rf(amount, r_quan, t_quan):
   
    return f'Php. {"{:.2f}".format(float(amount) * (((float(r_quan)/float(t_quan)) * 60)/100))}'

@register.simple_tag
def calc_rf2(amount, r_quan, t_quan):
   
    return float("{:.2f}".format(float(amount) * (((float(r_quan)/float(t_quan)) * 60)/100)))

@register.filter()
def received_or_not(value):
    if value == 1 or value == "1":
        return "Received"
    else:
        return "Ongoing"

@register.filter()
def accept_format(value):
    if value == 1 or value == "1":
        return "Accepted"
    elif value == 0 or value == "0":
        return "No Action"
    else:
        return "Declined"

@register.filter()
def total_redelivery_loss(a, b):
    try:
        return float(a) * float(b)
    except:
        return "ERROR"

@register.simple_tag
def calc_total_income(total_amount, cancel_refund_amount ,refund_amount, returned_quantity, price_per_unit):
    try:
        total_amount = float(total_amount)
    except:
        total_amount = 0
    try:
        delivery_fee = float(delivery_fee)
    except:
        delivery_fee = 0
    try:
        cancel_refund_amount = float(cancel_refund_amount)
    except:
        cancel_refund_amount = 0
    try:
        refund_amount = float(refund_amount)
    except:
        refund_amount = 0
    try:
        returned_quantity = float(returned_quantity)
    except:
        returned_quantity = 0

    try:
        price_per_unit = float(price_per_unit)
    except:
        price_per_unit = 0


    return f'Php. {"{:.2f}".format((total_amount)-(cancel_refund_amount)-(refund_amount))}'

@register.filter()
def month_yr_format(value):
    try:
        return value.strftime('%B %Y')
    except:
        date = datetime.strptime(value, '%Y-%m-%d')
        return date.strftime('%B %Y')


@register.filter()
def balance_format(a):
    if a == "" or a == None:
        return a 
    elif float(a) <= 0:
        return "Fully Paid"
    return f'Php. {"{:.2f}".format(float(a))}'
    

@register.filter()
def sold_out(a):
    try:
        a = float(a)
        if a <= 0 :
            return True
        else:
            return str(a)
    except:
        return a

@register.filter()
def is_confirm2(a):
    if a == 2 or a == "2":
        return "Declined"
    else:
        return "No response yet"


@register.filter()
def is_confirm(a):
    if a == None:
        return "Not yet paid"
    else:
        return "Paid"



    



    

    

    