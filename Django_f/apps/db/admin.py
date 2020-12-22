from django.contrib import admin
from apps.db.models import Set
# Register your models here.
class SetAdmin(admin.ModelAdmin):
 list_display = ['setname', 'setvalue','id']
admin.site.register(Set, SetAdmin)