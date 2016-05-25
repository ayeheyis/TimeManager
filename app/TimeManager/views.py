from django.shortcuts import render
from django.http import HttpResponse,Http404
from .task_view import *
from .forms import *
from django.shortcuts import redirect
from django.db import transaction
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

@transaction.atomic
def register(request):
    context = {}
    #User requested the register page
    if request.method == 'GET':
        context['register_user_form'] = RegisterUserForm()
        return render(request, 'register.html', context)

    #Build form from requests and validate
    form = RegisterUserForm(request.POST)
    if not form.is_valid():
        context['register_user_form'] = form
        return render(request, 'register.html', context)

    #Create new user with the valid inputs and save
    new_user = User.objects.create_user(username=form.cleaned_data['username'], \
                                      password=form.cleaned_data['password'])
    new_user.first_name = form.cleaned_data['first_name']
    new_user.last_name = form.cleaned_data['last_name']
    new_user.save()

    #Login new user
    new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
    login(request, new_user)

    return redirect('home')

@login_required
def home(request):
    context = {}
    return render(request, 'home.html', context)