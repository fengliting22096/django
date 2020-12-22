from django.contrib import admin
from apps.message.models import Product
from apps.apitest.models import Apis
from apps.apptest.models import Appcase
from apps.webtest.models import Webcase
class ProductAdmin(admin.ModelAdmin):
 list_display = ['productname', 'productdesc', 'producter','create_time','id']
admin.site.register(Product, ProductAdmin)

class ApisAdmin(admin.TabularInline):
 list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','Product']
 model = Apis
 extra = 1
class ProductAdmin(admin.ModelAdmin):
 list_display = ['productname', 'productdesc','create_time','id']
 inlines = [ApisAdmin]

class AppcaseAdmin(admin.TabularInline):
 list_display = ['appcasename', 'apptestresult','create_time','id','product']
 model = Appcase
 extra = 1
class ProductAdmin(admin.ModelAdmin):
 list_display = ['productname', 'productdesc','create_time','id']
 inlines = [AppcaseAdmin]

class WebcaseAdmin(admin.TabularInline):
 list_display = ['webcasename', 'webtestresult','create_time','id','product']
 model = Webcase
 extra = 1
class ProductAdmin(admin.ModelAdmin):
 list_display = ['productname', 'productdesc','create_time','id']
 inlines = [WebcaseAdmin]