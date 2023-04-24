from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .forms import *
from django.core import validators
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from parent.models import *

def index(request):
    return HttpResponse('under construction')

def registerSchool(request):
    form = RegisterSchoolForm()
    if request.method == 'POST':
        form = RegisterSchoolForm(request.POST)
        email = request.POST.get("email")
        try:
            validators.validate_email(email)
        except validators.ValidationError:
            messages.error(request, "Invalid email format.")
            return HttpResponseRedirect(reverse('registerParent'))
        if User.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'Email already exists. Please either login with this email or register with a new email.')
            return HttpResponseRedirect(reverse('registerSchool'))
        if form.is_valid():
            user = form.save()
            School.objects.create(user=user)
            messages.success(request, 'Account was created successfully')
            return HttpResponseRedirect(redirect_to=reverse('loginSchool'))
    context = {'form': form}
    return render(request, 'register_school.html', context)

def loginSchool(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, 'Username or password is incorrect.')
        else:
            login(request, user)
            if School.objects.get(user=request.user).name == "":
                return HttpResponseRedirect(redirect_to=reverse('schoolSettings'))
            else:
                return HttpResponseRedirect(redirect_to=reverse('dashboardSchool'))
    return render(request, 'login_school.html')

def logoutSchool(request):
    logout(request)
    return HttpResponseRedirect(redirect_to=reverse('loginSchool'))

def schoolSettings(request):
    form = SchoolForm(instance=request.user.school)
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES, instance=request.user.school)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to=reverse('dashboardSchool'))
    context = {'form': form}
    return render(request, 'school_settings.html', context)

def dashboardSchool(request):
    children = Child.objects.filter(school=request.user.school)
    approved_children = children.filter(is_approved=True)
    context = {'children': approved_children, 'school': request.user.school.name}
    return render(request, 'dashboard_school.html', context)

def childRequests(request):
    children = Child.objects.filter(school=request.user.school)
    pending_children = children.filter(is_approved=False)
    context = {'pending_children': pending_children}
    return render(request, 'child_requests.html', context)

def approveChild(request, pk):
    child = Child.objects.get(id=pk)
    child.is_approved = True
    child.save()
    return HttpResponseRedirect(redirect_to=reverse('childRequests'))

def dropChild(request, pk):
    child = Child.objects.get(id=pk)
    child.status = "Dismissed"
    child.save()
    return HttpResponseRedirect(redirect_to=reverse('dashboardSchool'))