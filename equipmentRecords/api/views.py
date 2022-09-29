from rest_framework import viewsets

from .models import Manager, Department, Device
from .serializers import ManagerSerializer, DepartmentSerializer, DeviceSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows managers to be viewed or edited.
     """
    queryset = Manager.objects.all().order_by('first_name', 'last_name')
    serializer_class = ManagerSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows departments to be viewed or edited.
     """
    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows managers to be viewed or edited.
     """
    queryset = Device.objects.all().order_by('name')
    serializer_class = DeviceSerializer
