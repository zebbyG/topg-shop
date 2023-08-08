from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('checkout/', views.check_out, name="checkout"),
    path('update_item/', views.update_item, name="update_item"),
    path('process_order/', views.process_order, name="process_order"),
    path('my_orders/', views.complete_orders, name="my_orders"),
    path('order_completed/', views.order_complete, name="order_completed"),
    path('leave_a_comment/', views.leave_comment, name="leave_a_comment")
    # path('delete_order/', views.delete_order, name='delete_order')
]
