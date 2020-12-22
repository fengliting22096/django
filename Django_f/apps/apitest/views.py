from django.shortcuts import render
from apps.apitest.models import Apitest, Apistep, Apis
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pymysql
# Create your views here.
# @login_required
def apitest_manage(request):
 apitest_list = Apitest.objects.all().order_by('id')  # 获取所有接口测试用例
 username = request.session['username'] # 读取浏览器登录 Session
 paginator = Paginator(apitest_list, 1)  # 生成 paginator 对象，设置每页显示 8 条记录
 page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第 1 页
 currentPage = int(page)  # 把获取的当前页码数转换成整数类型
 try:
  apitest_list = paginator.page(page)  # 获取当前页码数的记录列表
 except PageNotAnInteger:
  apitest_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
 except EmptyPage:
  apitest_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数# 中，则显示最后一a
 apitest_count = Apitest.objects.all().count() #统计产品数
 return render(request, "resources/apitest.html", {"user": username,"apitests":
apitest_list,"apitestcounts": apitest_count}) #把值赋给 apitestcounts 变量
# 接口步骤管理
# @login_required
def apistep_manage(request):
 username = request.session['username']
 apistep_list = Apistep.objects.all().order_by('id')
 paginator = Paginator(apistep_list, 8)  # 生成 paginator 对象，设置每页显示 8 条记录
 page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第 1 页
 currentPage = int(page)  # 把获取的当前页码数转换成整数类型
 try:
  apistep_list = paginator.page(page)  # 获取当前页码数的记录列表
 except PageNotAnInteger:
  apistep_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
 except EmptyPage:
  apistep_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，则显示最后一页内容
 apistep_count = Apistep.objects.all().count()  # 统计产品数
 return render(request, "resources/apistep.html", {"user": username,"apisteps": apistep_list,"apistepcounts": apistep_count})

# @login_required
def apimessage(request):
 username = request.session['username']
 apis_list = Apis.objects.all().order_by('id')
 paginator = Paginator(apis_list, 8)  # 生成 paginator 对象，设置每页显示 8 条记录
 page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第 1 页
 currentPage = int(page)  # 把获取的当前页码数转换成整数类型
 try:
  apis_list = paginator.page(page)  # 获取当前页码数的记录列表
 except PageNotAnInteger:
  apis_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
 except EmptyPage:
  apis_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，# 则显示最后一页内容
 apis_count = Apis.objects.all().count()  # 统计产品数
 return render(request, "resources/api.html", {"user": username, "apiss": apis_list, "apiscounts":
   apis_count})  # 把值赋给 apiscounts 变量

# @login_required
def test_report(request):
 username = request.session['username']
 apis_list = Apis.objects.all()
 apis_count = Apis.objects.all().count() #统计接口数
 db = pymysql.connect(user='root', db='django_f', passwd='root', host='127.0.0.1')
 cursor = db.cursor()
 sql1 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=1'
 aa=cursor.execute(sql1)
 apis_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]
 sql2 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=0'
 bb=cursor.execute(sql2)
 apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
 db.close()
 return render(request, "report/apitest_report.html", {"user": username,"apiss": apis_list,"apiscounts":
 apis_count,"apis_pass_counts": apis_pass_count,"apis_fail_counts": apis_fail_count}) #把值赋给apiscounts 变量

# 搜索功能
# @login_required
def apisearch(request):
 username = request.session['username'] # 读取浏览器登录 session
 search_apitestname = request.GET.get("apitestname", "")
 apitest_list = Apitest.objects.filter(apitestname__icontains=search_apitestname)
 return render(request,'resources/apitest.html', {"user": username,"apitests":apitest_list})

# 欢迎界面
# @login_required
def welcome(request):
 username = request.session['username']
 return render(request,'logo/welcome.html',{"user": username})