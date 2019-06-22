import json

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext

from core.models.employees import Employee, EmployeePassword, EmployeeSession
from organizations.forms.organization import OrganizationRegister

from lib.encryptation import encrypt, check_pw

def login(request):
    if request.method == 'GET':
        return render(request, "organizations/login.html")
    
    elif request.method == 'POST':
        login = request.POST

        employee = Employee.objects.filter(username=login.get('username')).first()

        if not employee:
            return JsonResponse({'error': True, 'msg': "Email or password don't match"})

        password = EmployeePassword.objects.filter(employee=employee).first()

        if not password:
            return JsonResponse({'error': True, 'msg': "Email or password don't match"})

        if check_pw(login.get('password'), password.password):
            session = EmployeeSession(employee=employee)
            session.save()

            return JsonResponse({
                'error': False,
                'msg': '',
                'contact': {
                    'id': employee.id,
                    'email': employee.email,
                    'first_name': employee.name,
                    'last_name': employee.last_name,
                    'phone': employee.phone
                },
                'session': session.get_values()
            })


def logout(request):
    return render(request, "onganizations/login.html")