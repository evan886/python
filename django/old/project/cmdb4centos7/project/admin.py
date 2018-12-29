from django.contrib import admin

# Register your models here.
from models import *

class appRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'availabity')

for cls in [app,app_roles]:
    admin.site.register(cls)
admin.site.register(appRole, appRoleAdmin)