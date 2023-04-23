from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .forms import RegisterParentForm
from django.core import validators
from django.contrib import messages
from .models import Parent, Child
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
            return HttpResponse("Account was created successfully")
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
            # return HttpResponseRedirect(reverse(''))
            return HttpResponse("Login successful")
    return render(request, 'login_parent.html')