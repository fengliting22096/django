from django.shortcuts import render
from apps.result.models import Bug
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# @login_required
def bug_manage(request):
 bug_list = Bug.objects.all().order_by('id')
 username = request.session['username']  # 读取浏览器登录 Session
 paginator = Paginator(bug_list, 1)  # 生成 paginator 对象，设置每页显示 8 条记录
 page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第 1 页
 currentPage = int(page)  # 把获取的当前页码数转换成整数类型
 try:
  bug_list = paginator.page(page)  # 获取当前页码数的记录列表
 except PageNotAnInteger:
  bug_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
 except EmptyPage:
  bug_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中， # 则显示最后一页的内容
 bug_count = Bug.objects.all().count()  # 统计 Bug 数
 return render(request, "resources/bug.html", {'user':username,"bugs": bug_list, "bugcounts":
  bug_count})  # 把值赋给 bugcounts 变量

# @login_required
def bugsearch(request):
 print(Bug.objects.all())
 username = request.session['username'] # 读取浏览器登录 Session
 search_bugname = request.GET.get("bugname", "")
 bug_list = Bug.objects.filter(bugname__icontains=search_bugname)
 return render(request,'resources/bug.html', {"user": username,"bugs":bug_list})

