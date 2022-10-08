from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from .models import Manager, Department, Device, Image
from .serializers import ManagerSerializer, DepartmentSerializer, DeviceSerializer, ListDeviceSerializer, \
    ListManagerSerializer, ListDepartmentSerializer, ImageSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all().order_by('first_name', 'last_name')
    serializer_class = ManagerSerializer
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        queryset = Manager.objects.all().order_by('first_name', 'last_name')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ListManagerSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        queryset = Department.objects.all().order_by('name')
        return queryset

    def list(self, request, *args, **kwargs):
        device_id = request.query_params.get('device_id', None)

        if not device_id:
            queryset = self.get_queryset()
            serializer = ListDepartmentSerializer(queryset, many=True, context={'request': request})
            return Response(serializer.data)
        else:
            try:
                int(device_id)
                device = get_object_or_404(Device, device_id=device_id)
                department = device.department
                serializer = ListDepartmentSerializer(department, many=False, context={'request': request})
                return Response(serializer.data)
            except ValueError:
                raise NotFound(detail="Wrong param value (device_id)", code=404)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('name')
    serializer_class = DeviceSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        queryset = Device.objects.all().order_by('name')
        return queryset

    def list(self, request, *args, **kwargs):
        department_id = request.query_params.get('department_id', None)

        if not department_id:
            queryset = self.get_queryset()
            serializer = ListDeviceSerializer(queryset, many=True, context={'request': request})
            return Response(serializer.data)
        else:
            try:
                int(department_id)
                department = get_object_or_404(Department, department_id=department_id)
                queryset = Device.objects.filter(department=department)
                serializer = ListDeviceSerializer(queryset, many=True, context={'request': request})
                return Response(serializer.data)
            except ValueError:
                raise NotFound(detail="Wrong param value (department_id)", code=404)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = (TokenAuthentication,)
