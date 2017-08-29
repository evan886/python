from django.contrib import admin

# Register your models here.
from  myapp.models import NewTable,Product


admin.site.register(NewTable)
admin.site.register(Product)