from django.contrib import admin
from . models import Employee, Tracking

# Register your models here.
MyModels=[Employee, Tracking]
admin.site.register(MyModels)