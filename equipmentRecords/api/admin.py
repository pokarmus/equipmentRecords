from django.contrib import admin

from .models import Manager, Department, Device

admin.site.register(Manager)
admin.site.register(Department)
admin.site.register(Device)
