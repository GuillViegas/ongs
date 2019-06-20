import json

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext

from core.models.employees import Employee, EmployeePassword, EmployeeSession
from organizations.forms.organization import OrganizationRegister

from lib.encryptation import encrypt, check_pw


def registerUser(request):
    if request.method == "GET":
        data = {}
        data['content_html'] = render(request, 'organizations/register/user.html', {}).content.decode("utf-8") 
        return HttpResponse(json.dumps(data), content_type='application/json')

    elif request.method == "POST":
        register_user = request.POST
        employee = Employee.objects.filter(email=register_user.get('email')).first()

        if employee:
            return JsonResponse({'error': 'Email already registered'})

        employee = Employee.objects.filter(username=register_user.get('username')).first()

        if employee:
            return JsonResponse({'error': 'Username already registered'})
        

        employee = Employee.objects.create(
            username=register_user.get('username'),
            name=register_user.get('first_name'),
            last_name=register_user.get('last_name'),
            email=register_user.get('email'),
            phone=register_user.get('phone'),
            organization=register_user.get('organization'),
            function=register_user.get('function'),
        )

        pw = EmployeePassword.objects.create(employee=employee, password=encrypt(register_user.get('password')))

        session = EmployeeSession(employee=employee)
        session.save()

        print(session.get_values())

        return JsonResponse({
            'session': session.get_values()['value']
        })


def registerOrganization(request):
    if request.method == "GET":
        data = {}

        data['content_html'] = render(request, 'organizations/register/organization.html', {
            'user': request.GET.get(''),
            'form': OrganizationRegister,
            }).content.decode("utf-8") 
        return HttpResponse(json.dumps(data), content_type='application/json')
        
    

def register(request):
    return render(request, "organizations/register/register.html")

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