from django.contrib import admin
from apps.result.models import Bug
# Register your models here.
class BugAdmin(admin.ModelAdmin):
 list_display = ['bugname', 'bugdetail', 'bugstatus', 'buglevel', 'bugcreater', 'bugassign','created_time','id']
admin.site.register(Bug, BugAdmin)