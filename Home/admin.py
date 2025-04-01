from django.contrib import admin
from .models import Package
from .models import Booking

class PackageAdmin(admin.ModelAdmin):
    list_display = ('pName', 'destination', 'hotel', 'days', 'nights', 'price', 'imgname')
    search_fields = ('pName', 'destination', 'hotel')   
    ordering = ('price',)  
admin.site.register(Package, PackageAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['package', 'user', 'numberofpeople', 'date', 'total_price', 'status']
    readonly_fields = ('total_price',)

admin.site.register(Booking,BookingAdmin)

