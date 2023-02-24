from django.contrib import admin
from hms.models import Booking
#admin.site.register(Booking) first way of registeration of model in adminpanel

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=['name','email','date','department','message']
