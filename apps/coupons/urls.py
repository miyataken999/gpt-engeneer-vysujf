from django.urls import path
from . import views

urlpatterns = [
    path('coupons/', views.coupon_list, name='coupon_list'),
    path('coupons/<pk>/', views.coupon_detail, name='coupon_detail'),
]