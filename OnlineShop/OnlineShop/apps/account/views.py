from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm, SignInForm

# Create your views here.

def register_view(request):
    context = {}

    if request.POST:
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('main')
        else:
            context['form'] = form
    else:
        context['form'] = SignUpForm()
    return render(request, 'register.html', context)

def sign_in_view(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect('main')

    if request.POST:
        form = SignInForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('main')

    else:
        form = SignInForm()

    context['form'] = form
    return render(request, 'sign_in.html', context)

def logout_view(request):
    logout(request)
    return redirect('main')