from django.urls import path
from apps.webtest import views

app_name = 'webtest'
urlpatterns = [
    path('webcase_manage/', views.webcase_manage, name='case'),
    path('webcasestep_manage/', views.webcasestep_manage, name='step'),
    path('websearch/', views.websearch, name='case'),
    path('webstepsearch/', views.webstepsearch, name='step'),

]