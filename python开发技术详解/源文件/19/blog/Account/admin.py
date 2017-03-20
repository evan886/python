from django.contrib import admin
from models import Account

#class AccountAdmin(admin.ModelAdmin):
#    list_display = ['name', 'password', 'email', 'desc']


#admin.site.register(Account, AccountAdmin)

admin.site.register(Account)