import json

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext

from core.models.employees import Employee, EmployeePassword, EmployeeSession
from core.models.organizations import Address, Organization
from organizations.forms.organization import AddressForm, OrganizationRegister

from lib.encryptation import encrypt, check_pw


def user(request):
    if request.method == "GET":
        data = {}
        data['content_html'] = render(request, 'organizations/register/user.html', {}).content.decode("utf-8") 
        return HttpResponse(json.dumps(data), content_type='application/json')

    elif request.method == "POST":
        user = request.POST
        employee = Employee.objects.filter(email=user.get('email')).first()

        if employee:
            return JsonResponse({'error': 'Email already registered'})

        employee = Employee.objects.filter(username=user.get('username')).first()

        if employee:
            return JsonResponse({'error': 'Username already registered'})
        

        employee = Employee.objects.create(
            username=user.get('username'),
            name=user.get('first_name'),
            last_name=user.get('last_name'),
            email=user.get('email'),
            phone=user.get('phone'),
            organization=user.get('organization'),
            function=user.get('function'),
        )

        pw = EmployeePassword.objects.create(employee=employee, password=encrypt(user.get('password')))

        session = EmployeeSession(employee=employee)
        session.save()

        return JsonResponse({
            'session': session.get_values()['value']
        })


def organization(request):
    if request.method == "GET":
        data = {}

        data['content_html'] = render(request, 'organizations/register/organization.html', {
            'form': OrganizationRegister,
            }).content.decode("utf-8") 
        return HttpResponse(json.dumps(data), content_type='application/json')

    elif request.method == "POST":
        data = request.POST
        organization = Organization.objects.filter(email=data.get('email')).first()

        if organization:
            return JsonResponse({'error': 'Email already registered'})

        employee = EmployeeSession.objects.filter(uuid=data.get('session_uuid')).first().employee

        organization = Organization.objects.create(
            name=data.get('name'),
            site=data.get('site'),
            presentation=data.get('presentation'),
            phones=[data.get('phone')],
            email=data.get('email'),
            action_areas=data.getlist('action_areas'),
        )

        employee.organization = organization
        employee.save()

        return JsonResponse({
            'organization': organization.get_values()
        })


def address(request):
    if request.method == "GET":
        data = {}

        data['content_html'] = render(request, 'organizations/register/address.html', {
            'form': AddressForm,
            }).content.decode("utf-8") 
        return HttpResponse(json.dumps(data), content_type='application/json')
    
    elif request.method == "POST":
        import ipdb ; ipdb.set_trace()
        data = request.POST

        address = Address.objects.create(
            cep=data.get('cep'),
            location=data.get('location'),
            number=data.get('number'),
            complement=data.get('complement'),
            neighborhood=data.get('neighborhood'),
            city=data.get('city'),
            state=data.get('state'),
        )

        organization = Organization.objects.filter(id=data.get('organization_id')).first()
        organization.address_id = address.id 
        organization.save()

        return JsonResponse({
            'reponse': 'ok'
        })

    

def main(request):
    return render(request, "organizations/register/register.html")