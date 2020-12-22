from django.contrib import admin
from apps.apitest.models import Apitest, Apistep, Apis
# Register your models here.

class ApistepAdmin(admin.TabularInline):
    list_display =\
        ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id', 'apitest']
    model = Apistep
    extra = 1


class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname', 'apitester', 'apitestresult', 'create_time', 'id']
    inlines = [ApistepAdmin]
admin.site.register(Apitest, ApitestAdmin)


class ApiAdmin(admin.ModelAdmin):
 list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','Product']
class ApisAdmin(admin.TabularInline):
 list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','Product']

admin.site.register(Apis, ApiAdmin)

admin.site.site_title = 'AutotestPlat'
admin.site.site_header = 'AtotestPlat'

