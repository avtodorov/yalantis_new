from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from autopark_app.models import Driver, Vehicle
from autopark_app.seriailizers import DriverSerializer, DriverDetailsSerializer, \
    VehicleSerializer, VehicleDetailsSerializer, UpdateSerializer

from django.shortcuts import get_object_or_404
from autopark_app.validator import date_format


# Create your views here.

# /drivers/driver/
class DriversList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    # sort by create_date:
    def get_queryset(self, *args, **kwargs):
        queryset = Driver.objects.all()
        query_gte = self.request.GET.get('created_at__gte')
        query_lte = self.request.GET.get('created_at__lte')

        if query_gte:
            queryset = Driver.objects.filter(created_at__gte=date_format(query_gte))
            # RETURNS DRIVERS CREATED AFTER "DATE"
        elif query_lte:
            queryset = Driver.objects.filter(created_at__lte=date_format(query_lte))
            # RETURNS DRIVERS CREATED BEFORE "DATE"
        else:
            return queryset

        return queryset


# /drivers/driver/<int:driver_id>
class DriverDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverDetailsSerializer

    def get_object(self):
        return get_object_or_404(Driver, pk=self.kwargs.get('driver_id'))


# /vehicles/vehicle/
class VehiclesList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Vehicle.objects.all()
        query = self.request.GET.get('with_drivers')
        if query:
            if query == 'yes':
                queryset = Vehicle.objects.filter(driver_id__isnull=False)
            if query == 'no':
                queryset = Vehicle.objects.filter(driver_id__isnull=True)
            return queryset

        return queryset


# /vehicles/vehicle/<int:vehicle_id>
class VehicleDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleDetailsSerializer

    def get_object(self):
        return get_object_or_404(Vehicle, pk=self.kwargs.get('vehicle_id'))


# /vehicles/set_driver/<int:vehicle_id>
#   "driver_id": PrimaryKeyRelatedField

class VehicleSetDriver(CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = UpdateSerializer

    def get(self, request, pk):
        vehicle = Vehicle.objects.get(id=pk)
        serializer = VehicleDetailsSerializer(vehicle)
        return Response(serializer.data)

    def create(self, request, pk):
        vehicle = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicle.driver_id_id = serializer.data["driver_id"]
        vehicle.save()

        return Response(VehicleDetailsSerializer(instance=vehicle).data)
