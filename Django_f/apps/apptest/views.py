from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.apptest.models import Appcase, Appcasestep
# Create your views here.
# app 用例管理
# @login_required
def appcase_manage(request):
 appcase_list = Appcase.objects.all().order_by('id')
 username = request.session['username'] # 读取浏览器登录 Session
 paginator = Paginator(appcase_list, 1)  # 生成 paginator 对象,设置每页显示 8 条记录
 page = request.GET.get('page', 1)  # 获取当前的页码数,默认为第 1 页
 currentPage = int(page)  # 把获取的当前页码数转换成整数类型
 try:
  appcase_list = paginator.page(page)  # 获取当前页码数的记录列表
 except PageNotAnInteger:
  appcase_list = paginator.page(1)  # 如果输入的页数不是整数则显示第 1 页的内容
 except EmptyPage:
  appcase_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数# 中则显示最后一页的内容
 appcase_count = Appcase.objects.all().count()  # 统计产品数
 return render(request, "apptest/testcase.html", {"user": username,"appcases":
  appcase_list, "appcasecounts": appcase_count})  # 把值赋给 appcasecounts 变量
# App 用例测试步骤
# @login_required
def appcasestep_manage(request):
 username = request.session['username']
 appcasestep_list = Appcasestep.objects.all().order_by('id')
 paginator = Paginator(appcasestep_list, 1)  # 生成 paginator 对象,设置每页显示 8 条记# 录
 page = request.GET.get('page', 1)  # 获取当前的页码数,默认为第 1 页
 currentPage = int(page)  # 把获取的当前页码数转换成整数类型
 try:
  appcasestep_list = paginator.page(page)  # 获取当前页码数的记录列表
 except PageNotAnInteger:
  appcasestep_list = paginator.page(1)  # 如果输入的页数不是整数则显示第 1 页的内容
 except EmptyPage:
  appcasestep_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统
 # 的页数中则显示最后一页
 return render(request, "apptest/testsep.html", {"user": username,"appcasesteps":
appcasestep_list})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 搜索功能
# @login_required
def appsearch(request):
 username = request.session['username'] # 读取浏览器登录 Session
 search_appcasename = request.GET.get("appcasename", "")
 appcase_list = Appcase.objects.filter(appcasename__icontains=search_appcasename)
 return render(request,'apptest/testcase.html', {"user": username,"appcases":appcase_list})
# 搜索功能
# @login_required
def appstepsearch(request):
 print(Appcasestep.objects.all())
 username = request.session['username']# 读取浏览器登录 Session
 search_appcasename = request.GET.get("appcasename", "")
 appcasestep_list = Appcasestep.objects.filter(apptestobjname__icontains=search_appcasename)
 return render(request,'apptest/testsep.html', {"user":
username,"appcasesteps":appcasestep_list})