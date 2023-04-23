from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .forms import *
from django.core import validators
from django.contrib import messages
from .models import Parent, Child
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def index(request):
    return HttpResponse('under construction')

def registerParent(request):
    form = RegisterParentForm()
    if request.method == 'POST':
        form = RegisterParentForm(request.POST)
        email = request.POST.get("email")
        try:
            validators.validate_email(email)
        except validators.ValidationError:
            messages.error(request, "Invalid email format.")
            return HttpResponseRedirect(reverse('registerParent'))
        if User.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'Email already exists. Please either login with this email or register with a new email.')
            return HttpResponseRedirect(reverse('registerParent'))
        if form.is_valid():
            user = form.save()
            Parent.objects.create(user=user)
            messages.success(request, 'Account was created successfully')
            return HttpResponseRedirect(redirect_to=reverse('loginParent'))
    context = {'form': form}
    return render(request, 'register_parent.html', context)

def loginParent(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, 'Username or password is incorrect.')
        else:
            login(request, user)
            return HttpResponseRedirect(redirect_to=reverse('dashboardParent'))
    return render(request, 'login_parent.html')

def logoutParent(request):
    logout(request)
    return HttpResponseRedirect(redirect_to=reverse('loginParent'))

def dashboardParent(request):
    children = Child.objects.filter(parent=Parent.objects.get(user=request.user))
    children = sorted(children, key=lambda x: x.is_approved, reverse=True)
    context = {'children': children}
    return render(request, 'dashboard_parent.html', context)

def createChild(request):
    form = CreateChildForm()
    if request.method == 'POST':
        form = CreateChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.parent = Parent.objects.get(user=request.user)
            child.save()
            messages.success(request, 'Child was created successfully')
            return HttpResponseRedirect(redirect_to=reverse('dashboardParent'))
    context = {'form': form}
    return render(request, 'create_child.html', context)