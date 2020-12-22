from django.urls import path
from apps.result import views

app_name = 'result'
urlpatterns = [
    path('bug_manage/', views.bug_manage, name='bug'),
    path('bugsearch/', views.bugsearch,name='search'),
]