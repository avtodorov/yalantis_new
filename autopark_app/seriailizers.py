
from rest_framework import serializers

from autopark_app.models import Driver, Vehicle


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    """Возвращает список водителей"""

    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'created_at', ]


class DriverDetailsSerializer(serializers.HyperlinkedModelSerializer):
    """Возвращает детали по конкретному водителю"""

    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'created_at', 'updated_at']


class DriverNestedSerializer(serializers.ModelSerializer):
    """Передает данные водителя в сериализаторы VehicleSerializer и VehicleDetailsSerializer"""

    class Meta:
        model = Driver
        fields = ['pk', 'first_name', 'last_name', ]


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    """Возвращает список автомобилей с информацией по водителям"""
    driver_id = DriverNestedSerializer(read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'driver_id', 'make', 'model', 'plate_number', ]


class VehicleDetailsSerializer(serializers.HyperlinkedModelSerializer):
    """Возвращает информацию по конкретному автомобилю с информацией по водителю"""
    driver_id = DriverNestedSerializer(read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'driver_id', 'make', 'model', 'plate_number', 'created_at', 'updated_at', ]


# _________________________________________________________________________________________________ #
# POST to set up the driver

class UpdateSerializer(serializers.Serializer):
    """Апдейт сериализатор для VehicleSetDriver"""
    driver_id = serializers.PrimaryKeyRelatedField(
        queryset=Driver.objects.all(), allow_null=True
    )
