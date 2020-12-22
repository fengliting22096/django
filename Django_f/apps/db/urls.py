from django.urls import path
from apps.db import views

app_name = 'db'
urlpatterns = [
    path('', views.set_manage, name='db_set'),
    path('user/', views.set_user, name='db_user'),

]