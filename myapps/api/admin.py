from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
from django.contrib import admin
from myapps.api.models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'color','brand']
    list_filter = ['brand','color']
    search_fields = ['name', 'color','brand']

admin.site.register(Car, CarAdmin)



TokenAdmin.raw_id_fields = ['user']