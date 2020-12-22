from django.shortcuts import render
from apps.message.models import Product
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# @xframe_options_exempt
# @login_required
def sign(request):
    """
    登陆处理
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username']=username
        request.session['password']=password
        product_list = Product.objects.all()
        return render(request, 'logo/HOME.html', {"user": username,"products": product_list})

    if request.method == 'GET':
        return render(request,'logo/sign.html')


def logout(request):
 return render(request.session.flush(),'logo/sign.html')

def left(request):
    return render(request, 'logo/left.html')



# @login_required
def apitest_manage(request):
    if request.method == 'GET':
        return render(request,'logo/sign.html')
    if request.method == 'POST':
        username = request.session['username']
        print(username)
        product_list = Product.objects.all()
        return render(request, 'resources/apitest.html',{"user": username,"products": product_list})



#产品管理
@xframe_options_exempt
# @login_required
def product_manage(request):
     product_list = Product.objects.all().order_by('id')
     product_count = Product.objects.all().count()
     paginator = Paginator(product_list, 8) #生成 paginator 对象，设置每页显示 8 条记录
     page = request.GET.get('page',1) #获取当前的页码数,默认为第 1 页
     currentPage=int(page) #把获取的当前页码数转换成整数类型
     username = request.session['username']
     try:
        product_list = paginator.page(page)#获取当前页码数的记录列表
     except PageNotAnInteger:
        product_list = paginator.page(1)#如果输入的页数不是整数，则显示第 1 页内容
     except EmptyPage:
        product_list = paginator.page(paginator.num_pages)#如果输入的页数不在系统的页数# 中，则显示最后一页内容
     return render(request, "logo/proc.html", {"user": username,"products": product_list,"productcounts": product_count})

# @login_required
def productsearch(request):
 username = request.session['username'] # 读取浏览器登录 Session
 search_productname = request.GET.get("productname", "")
 product_list = Product.objects.filter(productname__icontains=search_productname)
 return render(request,'logo/proc.html', {"user": username,"products":product_list})

def task(request):
    username = request.session['username']  # 读取浏览器登录 Session
    return render(request, 'logo/task.html',{"user": username})
from django.core.cache import cache
from django.shortcuts import HttpResponse
import time
import json
def test(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        time.sleep(0.05)
        cache.set(body['bindid'],body['timestmp'],timeout=body['timeout'])
        return HttpResponse(body['bindid'])
    if request.method == 'GET':
        return HttpResponse('参数异常')


def query(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        return HttpResponse(cache.get(body['bindid']))
    if request.method == 'GET':
        return HttpResponse('参数异常')