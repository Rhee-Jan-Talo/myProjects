from django.contrib import admin

# Register your models here.
########################################
from .models import Event
admin.site.register(Event)
########################################
from .models import user_account
admin.site.register(user_account)

from .models import user_order_request
admin.site.register(user_order_request)

from .models import payments
admin.site.register(payments)

from .models import purchase_history
admin.site.register(purchase_history)


from .models import req_redelivery
admin.site.register(req_redelivery)

from .models import req_refund
admin.site.register(req_refund)

from .models import payment_method_for_refund
admin.site.register(payment_method_for_refund)

from .models import user_order_confirmed
admin.site.register(user_order_confirmed)

from .models import payment_methods
admin.site.register(payment_methods)

from .models import delivery_info_details
admin.site.register(delivery_info_details)

from .models import refund_info
admin.site.register(refund_info)

from .models import confirm_refund
admin.site.register(confirm_refund)

from .models import model_redelivery_details
admin.site.register(model_redelivery_details)

from .models import redelivery_info_update
admin.site.register(redelivery_info_update)

from .models import announcement
admin.site.register(announcement)

from .models import address
admin.site.register(address)



