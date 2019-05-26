from django.shortcuts import render, redirect, reverse


def register(request):
    return render(request, "organizations/register.html")

def login(request):
    return render(request, "organizations/login.html")

def logout(request):
    return render(request, "onganizations/login.html")