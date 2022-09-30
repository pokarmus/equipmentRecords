from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Manager(models.Model):
    manager_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Department(models.Model):
    department_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name} - {self.manager}'


class Device (models.Model):
    device_id = models.BigAutoField(primary_key=True)
    barcode = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.barcode}'

