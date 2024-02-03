from django.urls import path
from .views import order_product, order_list, update_order, delete_order
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/', order_product, name='order_product'),
    path('order_list/', order_list, name='order_list'),
    path('update_order/<int:order_id>/', update_order, name='update_order'),
    path('delete_order/<int:order_id>/', delete_order, name='delete_order'),

]