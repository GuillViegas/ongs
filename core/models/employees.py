from django.db import models
from core.models.organizations import Organization

from datetime import timedelta
import uuid

SESSION_DURATION = 7


class Employee(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    organization = models.ForeignKey(Organization, related_name='employees', on_delete=models.CASCADE, null=True, blank=True)
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


class EmployeeSession(models.Model):
    class Meta:
        unique_together = ("uuid", "created_at")

    employee = models.ForeignKey(Employee, related_name='employee_session', on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)

    def get_values(self):
        return {
            'error': False,
            'msg': '',
            'value': {
                'full_name': '{} {}'.format(self.employee.name, self.employee.last_name),
                'email': self.employee.email,
                'uuid': self.uuid,
                'created_at': self.created_at,
                'expires_at': self.created_at + timedelta(days=SESSION_DURATION)
            }
        }