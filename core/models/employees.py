from django.db import models
from core.models.organizations import Organization


class Employee(models.Model):
    username = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    organization = models.ForeignKey(Organization, related_name='employee', on_delete=models.CASCADE)
    function = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return 'Employee #{}: {}'.format(self.id, self.email)


class EmployeePassword(models.Model):
    class Meta:
        verbose_name = 'Employee: EmployeePassword'

    employee = models.ForeignKey(Employee, related_name='employee_password', on_delete=models.CASCADE)
    password = models.CharField(max_length=60)

    def __str__(self):
        return 'EmployeePassword #{}: ({})'.format(self.id, self.employee_id)