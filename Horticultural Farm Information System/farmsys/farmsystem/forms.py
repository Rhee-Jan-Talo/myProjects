from django import forms

from .models import *




class user_accForm(forms.ModelForm):
	class Meta:
		model = user_account
		fields = ['username','passw','confirm_passw','phone_num']

class user_accFormEmail(forms.ModelForm):
	class Meta:
		model = user_account
		fields = ['username','passw','confirm_passw','email_ad']
			
class user_accForm2(forms.ModelForm):
	class Meta:
		model = user_account
		fields = ['full_name','adress','phone_num','comp', 'email_ad']

class requestForm(forms.ModelForm):
	class Meta:
		model = user_order_request
		#fields = ['user_id','harvest_id', 'plant_name', 'grade', 'quantity', 'units', 'date_needed', 'is_admin_approved', 'desc']

		fields = ['user_id','harvest_id', 'plant_name', 'quantity', 'date_needed']

class paymentForm(forms.ModelForm):
	class Meta:
		model = payments
		fields = ['p_id','payment_for','proof_receipt','amount_paid']

class historyForm(forms.ModelForm):
	class Meta:
		model = purchase_history
		fields = ['transaction_id','user_id','feedback']

class rdForm(forms.ModelForm):
	class Meta:
		model = req_redelivery
		fields = ['transac_id','quan_received','units', 'returned_quan','reason_rd','proof_pic']

class refundForm(forms.ModelForm):
	class Meta:
		model = req_refund
		fields = ['transac_id','quantity_received','units','refund_quan','reason_refund','proof_refund']

class refundPMForm(forms.ModelForm):
	class Meta:
		model = payment_method_for_refund
		fields = ['purchase_history_id','payment_method','payment_for','account_num','account_name']


class confirmForm(forms.ModelForm):
	class Meta:
		model = user_order_confirmed
		fields = ['u_order_id','harvest_id','plant_name','confirmed_quantity','units','total_amount','total_downpayment','dp_due','expected_date_arrival','delivery_fee','balance_to_pay'] 
		
	    
class paymentmethodsForm(forms.ModelForm):
	class Meta:
		model = payment_methods
		fields=['f_order_id','payment_method','account_number','account_name']

class paymentmethodsFormEdit(forms.ModelForm):
	class Meta:
		model = payment_methods
		fields=['f_order_id','payment_method','account_number','account_name'  ]


class adminpaymentmethodsForm(forms.ModelForm):
	class Meta:
		model = payment_methods
		fields=['for_admin','payment_method','account_number','account_name'  ]

class deliveryinfoForm(forms.ModelForm):
	class Meta:
		model = delivery_info_details
		fields=['f_order_id','delivery_status','details','date_arrived']

class refunddetailsForm(forms.ModelForm):
	class Meta: 
		model = refund_info
		fields=['f_order_id','date_from','date_to','refund_percentage']

class refunddetailsEdit(forms.ModelForm):
	class Meta: 
		model = refund_info
		fields=['date_from','date_to','refund_percentage']
		
class refundPaymentForm(forms.ModelForm):
	class Meta:
		model = confirm_refund
		fields=['refund_amount', 'proof_of_refund']

class redeliverydetailsForm(forms.ModelForm):
	class Meta:
		model = model_redelivery_details
		fields = ['harvest_id','quantity_variations_id','quantity_delivered']

class redeliveryUpdateForm(forms.ModelForm):
	class Meta:
		model = redelivery_info_update
		fields = ['re_delivery_status','details']

class announcementForm(forms.ModelForm):
	class Meta:
		model = announcement
		fields = ['a_title','a_link','a_desc','a_days']

class addressForm(forms.ModelForm):
	class Meta:
		model = address
		fields = ['lot','street','city','province','zipcode','block','barangay']