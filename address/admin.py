from django.contrib import admin

# Register your models here.
from address.models import Delivery, Address

class AdressAdmin(admin.TabularInline):
    model = Address

class DeliveryAdmin(admin.ModelAdmin):
   inlines = [AdressAdmin,]

admin.site.register(Delivery,DeliveryAdmin)