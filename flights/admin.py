from django.contrib import admin

from .models import Flight, Airport,Passenger

# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)

admin.site.register(Airport)

admin.site.register(Passenger,PassengerAdmin)


admin.site.register(Flight,FlightAdmin)



# # Register your models here.

# admin.site.register(FlightAdmin)