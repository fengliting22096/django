from django.shortcuts import render
from apps.db.models import Set
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# @login_required
def set_manage(request):
 set_list = Set.objects.all().order_by('id')
 username = request.session['username']
 paginator = Paginator(set_list, 8)  # 生成 paginator 对象，设置每页显示 8 条记录
 page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第 1 页
 currentPage = int(page)  # 把获取的当前页码数转换成整数类型
 try:
  set_list = paginator.page(page)  # 获取当前页码数的记录列表
 except PageNotAnInteger:
  set_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
 except EmptyPage:
  set_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，
 return render(request, "resources/db.html", {'user':username,"sets": set_list})
# @login_required
def set_user(request):
 user_list = User.objects.all()
 username = request.session['username']
 return render(request, "resources/db_user.html", {'user':username,"users": user_list})