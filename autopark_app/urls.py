from django.urls import path
from autopark_app import views

app_name = 'autopark_app'

urlpatterns = [
    # DRIVERS
    path('drivers/driver/', views.DriversList.as_view(), name='DriversList'),
    path('drivers/driver/<int:driver_id>', views.DriverDetails.as_view(), name='DriverDetails'),

    # VEHICLES
    path('vehicles/vehicle/', views.VehiclesList.as_view(), name='VehiclesList'),
    path('vehicles/vehicle/<int:vehicle_id>', views.VehicleDetails.as_view(), name='VehicleDetails'),
    path('vehicles/set_driver/<pk>', views.VehicleSetDriver.as_view(), name='SetDriver'),

]
