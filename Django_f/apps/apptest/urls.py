from django.urls import path
from apps.apptest import views

app_name = 'apptest'
urlpatterns = [
    path('appcase_manage/', views.appcase_manage, name='case'),
    path('appcasestep_manage/', views.appcasestep_manage, name='step'),
    path('appsearch/', views.appsearch, name='case'),
    path('appstepsearch/', views.appstepsearch, name='step'),

]