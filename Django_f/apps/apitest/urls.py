from django.urls import path
from apps.apitest import views

app_name = 'apitest'
urlpatterns = [
    path('', views.apimessage, name='api'),
    path ('test_report/', views.test_report, name='report'),
    path('apitest_manage/', views.apitest_manage, name='test'),
    path('apistep_manage/', views.apistep_manage, name='step'),
    path('apisearch/', views.apisearch, name='step'),
    path('welcome/', views.welcome, name='welcome'),

]