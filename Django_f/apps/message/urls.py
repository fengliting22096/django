from django.urls import path
from apps.message import views

app_name = 'resources'
urlpatterns = [
    path('', views.product_manage, name='product'),
    path('tasks/', views.task, name='task'),
    path('logout/', views.logout, name='logout'),
    path('sign/', views.sign, name='sign'),
    path('left/', views.left, name='left'),
    path('apitest_manage/', views.apitest_manage, name='apitest_manage'),
    path('productsearch/', views.productsearch,name='search'),
    path('test/', views.test,name='test'),
    path('query/', views.query,name='query'),
]