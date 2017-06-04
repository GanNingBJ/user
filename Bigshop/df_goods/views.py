#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import *
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    typelist=TypeInfo.objects.all()
    list=[]
    for type in typelist:
        list.append({
            'type':type,
            'click_list':type.goodsinfo_set.order_by('-gclick')[0:3],
            'new_list':type.goodsinfo_set.order_by('-id')[0:4]
        })
    context={'title':'首页','list':list}
    return render(request,'df_goods/index.html',context)

def index2(request,tid):
    #查询点击最高、最新的商品
    t1_click= GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')[0:3]
    t1_new=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')[0:4]
    #构造点击量最高的商品列表
    click_list=[]
    for click in t1_click:
        click_list.append({'id':click.id,'title':click.gtitle})
    #构造最新的商品列表
    new_list=[]
    for new in t1_new:
        new_list.append({'id':new.id,'title':new.gtitle,'price':new.gprice,'pic':new.gpic.name})
    #返回json
    context={'click_list':click_list,'new_list':new_list}
    return JsonResponse(context)

def list(request,tid,pindex,orderby):
    gtype=TypeInfo.objects.get(id=int(tid))
    #查询两条最新的数据
    new_list=gtype.goodsinfo_set.order_by('-id')[0:2]
    #查询指定分类tid的商品
    goods_list=gtype.goodsinfo_set.all()
    #根据指定规则排序
    if orderby=='1':
        goods_list=goods_list.order_by('-id')
    elif orderby=='2':
        goods_list=goods_list.order_by('-gprice')
    elif orderby=='3':
        goods_list=goods_list.order_by('-gclick')
    #进行分页
    paginator=Paginator(goods_list,10)
    pindex2=int(pindex)
    if pindex2<=0:
        pindex2=1
    elif pindex2>paginator.num_pages:
        pindex2=paginator.num_pages
    page=paginator.page(pindex2)
    context={'title':'列表页','page':page,
             'tid':tid,'gtype':gtype,'orderby':orderby,
             'new_list':new_list}
    return render(request,'df_goods/list.html',context)


def detail(request,gid):
    goods=GoodsInfo.objects.get(pk=gid)
    goods.gclick=goods.gclick+1
    goods.save()
    new_list=goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context={'title':'商品详情','goods':goods,
             'new_list':new_list}
    return render(request,'df_goods/detail.html',context)