from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.webtest.models import Webcase, Webcasestep
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# @login_required
def webcase_manage(request):
 webcase_list = Webcase.objects.all().order_by('id')
 username = request.session['username'] # 读取浏览器登录 Session
 paginator = Paginator(webcase_list, 1)  # 生成 paginator 对象，设置每页显示 8 条记录
 page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第 1 页
 currentPage = int(page)  # 把获取的当前页码数转换成整数类型
 try:
  webcase_list = paginator.page(page)  # 获取当前页码数的记录列表
 except PageNotAnInteger:
  webcase_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页的内容
 except EmptyPage:
  webcase_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数# 中，则显示最后一页
 webcase_count = Webcase.objects.all().count()  # 统计产品数
 return render(request, "webtest/case.html", {'user':username,"webcases":
  webcase_list, "webcasecounts": webcase_count})  # 把值赋给 webcasecounts 变量
# Web 用例测试步骤
# @login_required
def webcasestep_manage(request):
 username = request.session['username']
 webcasestep_list = Webcasestep.objects.all().order_by('id')
 paginator = Paginator(webcasestep_list, 1)  # 生成 paginator 对象，设置每页显示 8 条 # 记录
 page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第 1 页
 currentPage = int(page)  # 把获取的当前页码数转换成整数类型
 try:
  webcasestep_list = paginator.page(page)  # 获取当前页码数的记录列表
 except PageNotAnInteger:
  webcasestep_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
 except EmptyPage:
  webcasestep_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统
 # 的页数中，则显示最后一页内容
 return render(request, "webtest/step.html", {"user": username,"webcasesteps": webcasestep_list})

# 搜索功能
# @login_required
def websearch(request):
 username = request.session['username'] # 读取浏览器登录 Session
 search_webcasename = request.GET.get("webcasename", "")
 webcase_list = Webcase.objects.filter(webcasename__icontains=search_webcasename)
 return render(request,'webtest/case.html', {"user": username,"webcases":webcase_list})
# 搜索功能
# @login_required
def webstepsearch(request):

 username = request.session['username']# 读取浏览器登录 Session
 search_webcasename = request.GET.get("webcasename", "")
 webcasestep_list = Webcasestep.objects.filter(webcasename__icontains=search_webcasename)
 return render(request,'webtest/step.html', {"user":
username,"webcasesteps":webcasestep_list})