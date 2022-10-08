from django.contrib import admin

from .models import Manager, Department, Device, Image

admin.site.register(Manager)
admin.site.register(Department)
admin.site.register(Device)
admin.site.register(Image)
