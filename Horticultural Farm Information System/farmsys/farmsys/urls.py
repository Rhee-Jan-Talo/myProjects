
from django.contrib import admin
from django.urls import path
from farmsystem import views as farmsys_views
import random

codee = str(random.randint(0,999999))

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('', include('theblog.urls')),
    path('', farmsys_views.login_page, name='login_page'),

    path('login_admin', farmsys_views.login_admin, name='login_admin'),
    path('about_us', farmsys_views.about_us, name='about_us'),
    path('home/', farmsys_views.home, name='home'),
    path('home_admin/', farmsys_views.home_admin, name='home_admin'),
    path('logout_user/', farmsys_views.logout_user, name='logout_user'),
    path('register_phone/', farmsys_views.register_phone, name="register_phone"),
    path('register_email/', farmsys_views.register_email, name="register_email"),
    path(f'confirm_phone/{codee}{codee}<code>{codee}', farmsys_views.confirm_phone, name="confirm_phone"),
    path(f'confirm_email/{codee}{codee}<code>{codee}', farmsys_views.confirm_email, name="confirm_email"),
    path('final_registration/<user_id>', farmsys_views.final_registration, name="final_registration"),
    path('edit_shipping_address', farmsys_views.edit_shipping_address, name='edit_shipping_address'),    
    path('change_password', farmsys_views.change_password, name='change_password'),
    path('tbc_admin/', farmsys_views.tbc_admin, name="tbc_admin"),
    path('tbc_user/', farmsys_views.tbc_user, name="tbc_user"),
    path('sales_order/<message>', farmsys_views.sales_order, name="sales_order"),
    path('success_orders/', farmsys_views.success_orders, name="success_orders"),
    path('cancelled_orders/', farmsys_views.cancelled_orders, name="cancelled_orders"),
    path('refund/', farmsys_views.refund, name="refund"),
    path('redelivery/', farmsys_views.redelivery, name="redelivery"),
    path('browse_plants/', farmsys_views.browse_plants, name="browse_plants"),
    path('plant_details/<harvest_id>', farmsys_views.plant_details, name="plant_details"),

    path('tabular_form/<t_type>', farmsys_views.tabular_form, name="tabular_form"),

    #path('growth_details/', farmsys_views.growth_details, name="growth_details"),
    path('purchase_plant/<harvest_id>', farmsys_views.purchase_plant, name="purchase_plant"),
    path('tbc_user_details/<u_order_id>', farmsys_views.tbc_user_details, name="tbc_user_details"),
    path('payment/<pmethod>/<p_id>', farmsys_views.payment, name="payment"),
    path('sales_order_details/<f_order_id>', farmsys_views.sales_order_details, name="sales_order_details"),
    path('delivery_info/<f_order_id>', farmsys_views.delivery_info, name="delivery_info"),
    path('tbc_admin_details/<order_id>', farmsys_views.tbc_admin_details, name="tbc_admin_details"),
    path('success_orders_details/<f_order_id>', farmsys_views.success_orders_details, name="success_orders_details"),
    path('cancelled_orders_details/<f_order_id>', farmsys_views.cancelled_orders_details, name="cancelled_orders_details"),
    path('refund_form/<purchase_history_id>', farmsys_views.refund_form, name="refund_form"),
    path('refund_details/<refund_id>', farmsys_views.refund_details, name="refund_details"),
    path('pm_refund/<purchase_history_id>', farmsys_views.pm_refund, name="pm_refund"),

    path('pm_refund_order/<f_order_id>', farmsys_views.pm_refund_order, name="pm_refund_order"),
    
    
    path('redelivery_form/<purchase_history_id>', farmsys_views.redelivery_form, name="redelivery_form"),

    path('redelivery_details/<purchase_history_id>', farmsys_views.redelivery_details, name="redelivery_details"),

    path('redelivery_info/<rd_id>', farmsys_views.redelivery_info, name="redelivery_info"),
    path('confirm_user/<f_order_id>', farmsys_views.confirm_user, name="confirm_user"),
    #path('/', farmsys_views., name=""),
    path('profile/', farmsys_views.profile, name="profile"),
    path('set_sh_address_default/<address_id>', farmsys_views.set_sh_address_default, name="set_sh_address_default"),
    ######################ADMIN######################
    path('admin_order_requests/',  farmsys_views.admin_order_requests, name="admin_order_requests"),
    path('admin_refund_requests/',  farmsys_views.admin_refund_requests, name="admin_refund_requests"),
    path('admin_refund_action/<refund_id>',  farmsys_views.admin_refund_action, name="admin_refund_action"),
    path('admin_refund_update/<refund_id>',  farmsys_views.admin_refund_update, name="admin_refund_update"),
    path('decline_refund/<refund_id>',  farmsys_views.decline_refund, name="decline_refund"),

    path('decline_redelivery/<re_delivery_id>',  farmsys_views.decline_redelivery, name="decline_redelivery"),
    
    path('pay_order_refund/<pmfr_id>',  farmsys_views.pay_order_refund, name="pay_order_refund"),

    path('admin_redelivery_requests/',  farmsys_views.admin_redelivery_requests, name="admin_redelivery_requests"),

    path('admin_cancelled_orders/',  farmsys_views.admin_cancelled_orders, name="admin_cancelled_orders"),
    path('admin_cancelled_orders_details/<f_order_id>',  farmsys_views.admin_cancelled_orders_details, name="admin_cancelled_orders_details"),
    
    path('admin_redelivery_details/<harvest_id>/<re_delivery_id>/<quantity_selected>',  farmsys_views.admin_redelivery_details, name="admin_redelivery_details"),

    path('admin_redelivery_info/<re_delivery_id>/<status>',  farmsys_views.admin_redelivery_info, name="admin_redelivery_info"),
    
    path('admin_redelivery_update/<re_delivery_id>', farmsys_views.admin_redelivery_update, name="admin_redelivery_update"),
    path('admin_order_action/<u_order_id>',  farmsys_views.admin_order_action, name="admin_order_action"),
    path('admin_order_update/<u_order_id>',  farmsys_views.admin_order_update, name="admin_order_update"),
    path('add_refund/<f_order_id>',  farmsys_views.add_refund, name="add_refund"),
    path('add_payment_method/<f_order_id>',  farmsys_views.add_payment_method, name="add_payment_method"),
    path('update_payment_method/<p_id>',  farmsys_views.update_payment_method, name="update_payment_method"),
    path('add_delivery_info/<f_order_id>',  farmsys_views.add_delivery_info, name="add_delivery_info"),
    path('view_delivery_info/<f_order_id>/<u_order_id>' , farmsys_views.view_delivery_info, name='view_delivery_info'), 
    path('edit_refund_info/<rd_id>',  farmsys_views.edit_refund_info, name="edit_refund_info"),
    
    path('view_only_order_details/<u_order_id>',  farmsys_views.view_only_order_details, name="view_only_order_details"),
    path('refund_payment/<pmfr_id>', farmsys_views.refund_payment, name="refund_payment"),
    path('admin_redelivery_action/<re_delivery_id>', farmsys_views.admin_redelivery_action, name="admin_redelivery_action"),

    path('decline_order_request/', farmsys_views.decline_order_request, name="decline_order_request"),

    path('confirm_payment_amount/<payment_done_id>', farmsys_views.confirm_payment_amount, name="confirm_payment_amount"),

    path('view_payment_done/<p_id>', farmsys_views.view_payment_done, name="view_payment_done"),
    path('add_deliv_info/<f_order_id>/<u_order_id>', farmsys_views.add_deliv_info, name="add_deliv_info"),
    path('add_redeliv_info/<re_delivery_id>', farmsys_views.add_redeliv_info, name="add_redeliv_info"),

    path('announcements_admin/', farmsys_views.announcements_admin, name="announcements_admin"),
    path('add_announcement/<action>/<a_id>', farmsys_views.add_announcement, name="add_announcement"),
    
    path('remove_to_view/<rtv_type>/<some_id>', farmsys_views.remove_to_view, name="remove_to_view"),
    path('back_to_view/<rtv_type>/<some_id>', farmsys_views.back_to_view, name="back_to_view"),
    path('removed_from_view/<r_type>', farmsys_views.removed_from_view, name="removed_from_view"),
    path('received_orders/', farmsys_views.received_orders, name="received_orders"),
    path('admin_payment_methods/', farmsys_views.admin_payment_methods, name="admin_payment_methods"),
    path('add_admin_payment_method/<add_type>/<p_id>', farmsys_views.add_admin_payment_method, name="add_admin_payment_method"),
    path('sales_summary/', farmsys_views.sales_summary, name="sales_summary"),
    path('refund_rules/', farmsys_views.refund_rules, name="refund_rules"),
    ######################



    #path('changecalendar/<month>/<year>' , prof_views.changecalendar, name='changecalendar'), #
    #path('growth_details/' , farmsys_views.CalendarView.as_view(), name='growth_details'), 
    path('growth_details/<batch_id>/' , farmsys_views.growth_details, name='growth_details'), 
    path('prev_month/<curr_date>/<batch_id>/' , farmsys_views.prev_month, name='prev_month'), 
    path('next_month/<curr_date>/<batch_id>/' , farmsys_views.next_month, name='next_month'), 


    path('user_soa/' , farmsys_views.user_soa, name='user_soa'), 
    path('user_refunds/' , farmsys_views.user_refunds, name='user_refunds'), 
    path('user_deliveries/' , farmsys_views.user_deliveries, name='user_deliveries'), 
    path('soa_billing/<f_order_id>' , farmsys_views.soa_billing, name='soa_billing'), 

  
]
