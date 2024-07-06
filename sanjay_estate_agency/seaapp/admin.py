from django.contrib import admin
from .models import Property, RentalProperty


admin.site.register(Property)
admin.site.register(RentalProperty)