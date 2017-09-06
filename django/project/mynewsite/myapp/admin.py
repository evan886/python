from django.contrib import admin

# Register your models here.
from  myapp.models import NewTable,Product,Author


admin.site.register(NewTable)
admin.site.register(Product)
admin.site.register(Author)