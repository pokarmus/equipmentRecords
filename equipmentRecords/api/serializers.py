from rest_framework import serializers

from .models import Manager, Department, Device


class ManagerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Manager
        fields = ['manager_id', 'first_name', 'last_name', 'url']


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Department
        fields = ['department_id', 'name', 'manager']


class DeviceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Device
        fields = ['device_id', 'barcode', 'name', 'description', 'department']
