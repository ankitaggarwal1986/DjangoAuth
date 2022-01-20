from django.contrib import admin
from . models import Buyer,Machine,Sale

# Register your models here.
mymodels=[Buyer,Machine,Sale]
admin.site.register(mymodels)