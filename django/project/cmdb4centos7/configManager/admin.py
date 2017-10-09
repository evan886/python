from django.contrib import admin

# Register your models here.
from models import *

for cls in [config]:
    admin.site.register(cls)