from rest_framework import viewsets
from rest_framework.response import Response

from .models import Manager, Department, Device
from .serializers import ManagerSerializer, DepartmentSerializer, DeviceSerializer, ListDeviceSerializer, \
    ListManagerSerializer, ListDepartmentSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows managers to be viewed or edited.
     """
    queryset = Manager.objects.all().order_by('first_name', 'last_name')
    serializer_class = ManagerSerializer

    def get_queryset(self):
        queryset = Manager.objects.all().order_by('first_name', 'last_name')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ListManagerSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)


class DepartmentViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows departments to be viewed or edited.
     """
    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        queryset = Department.objects.all().order_by('name')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ListDepartmentSerializer(queryset, many=True, context={'request': request})


        return Response(serializer.data)


class DeviceViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows managers to be viewed or edited.
     """
    queryset = Device.objects.all().order_by('name')
    serializer_class = DeviceSerializer

    def get_queryset(self):
        queryset = Device.objects.all().order_by('name')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ListDeviceSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

