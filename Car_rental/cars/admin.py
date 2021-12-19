from django.contrib import admin
from.models import cars

# Register your models here.
class carsAdmin(admin.ModelAdmin):
    list_display=('name','price')

admin.site.register(cars,carsAdmin)