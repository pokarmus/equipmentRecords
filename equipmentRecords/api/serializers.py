from rest_framework import serializers

from .models import Manager, Department, Device


class ManagerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Manager
        fields = ['manager_id', 'first_name', 'last_name', 'phone_number']


class ListManagerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Manager
        fields = ['first_name', 'last_name', 'url']


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Department
        fields = ['department_id', 'name', 'manager']


class ListDepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Department
        fields = ['name', 'url']


class DeviceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Device
        fields = ['name', 'barcode', 'description', 'device_id', 'department']


class ListDeviceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Device
        fields = ['name', 'barcode', 'url']
