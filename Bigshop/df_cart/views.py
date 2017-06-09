#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from fresh.user_decorator import *
from models import *
from fresh.models import  *
# Create your views here.
@login
def add(request,gid,count):
    carts=CartInfo.objects.filter(goods_id=gid).filter(user_id=request.session['user_id'])
    if len(carts)==0:
        cart=CartInfo()
        cart.goods_id=int(gid)
        cart.user_id=request.session['user_id']
        cart.count=int(count)
        cart.save()
    else:
        cart=carts[0]
        cart.count+=int(count)
        cart.save()
    if request.is_ajax():
        return JsonResponse({'count':CartInfo.objects.filter(user_id=request.session['user_id']).count()})
    else:
        return redirect('/cart/')

@login
def list(request):
    cart_list=CartInfo.objects.filter(user_id=request.session['user_id'])
    context={
        'title':'购物车',
        'page_name':1,
        'cart_list':cart_list,
    }
    return render(request,'df_cart/cart.html',context)


def count_change(request):
    id=request.GET.get('id')
    count=request.GET.get('count')
    cart=CartInfo.objects.get(id=int(id))
    cart.count=int(count)
    cart.save()
    return JsonResponse({'count':cart.count})


def delete(request):
    id=request.GET.get('id')
    cart=CartInfo.objects.get(id=int(id))
    cart.delete()
    # 后端删除完之后传递给前段,让其在页面上删除
    return JsonResponse({'result':'ok'})

def order(request):
    user=UserInfo.objects.get(id=request.session['user_id'])
    cart_ids=request.GET.getlist('cart_id')
    carts=CartInfo.objects.filter(id__in=cart_ids)
    context={
        'title':'提交订单',
        'page_name':1,
        'user':user,
        'carts':carts,

    }
    return render(request,'df_cart/order.html',context)