from django.contrib import admin

from models import *

for cls in [dataCenter, asset]:
    admin.site.register(cls)