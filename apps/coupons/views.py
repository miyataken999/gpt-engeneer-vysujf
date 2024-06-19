from django.shortcuts import render
from .models import Coupon

def coupon_list(request):
    coupons = Coupon.objects.all()
    return render(request, 'coupon_list.html', {'coupons': coupons})

def coupon_detail(request, pk):
    coupon = Coupon.objects.get(pk=pk)
    return render(request, 'coupon_detail.html', {'coupon': coupon})