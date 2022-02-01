from django.contrib import admin
from autopark_app.models import Driver, Vehicle


# Register your models here.
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created_at', 'updated_at',)
    list_display_links = ('id',)
    search_fields = ('id', 'first_name', 'last_name', 'created_at', 'updated_at',)
    list_editable = ('first_name', 'last_name',)
    list_filter = ('id', 'first_name', 'last_name',)


admin.site.register(Driver, DriverAdmin)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver_id', 'make', 'plate_number', 'created_at', 'updated_at')
    list_display_links = ('id',)
    search_fields = ('id', 'driver_id', 'plate_number',)
    list_editable = ('driver_id',)
    list_filter = ('id', 'driver_id', 'make', 'plate_number',)


admin.site.register(Vehicle, VehicleAdmin)
