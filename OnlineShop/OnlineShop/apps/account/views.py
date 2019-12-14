from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def register_view(request):
    context = {}

    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
        else:
            context['form'] = form
    else:
        context['form'] = UserCreationForm()
    return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return redirect('main')