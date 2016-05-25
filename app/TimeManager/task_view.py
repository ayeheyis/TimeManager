from django.shortcuts import render
from django.http import HttpResponse,Http404
from .forms import *
from django.shortcuts import redirect
from django.db import transaction
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


@login_required
def task(request):
    context = {}
    return render(request, 'task.html', context)

@login_required
def task_form(request):
    context = {}
    if(request.method == 'GET'):
        return redirect('task')
    print request.POST
    if(validate_create(request)):
        return redirect('home')
    return redirect('task')

#############Helper Functions##############################
def validate_create(request):
    if(not('name' in request.POST and request.POST['name'])):
            return False
    if(not('description' in request.POST and request.POST['description'])):
            return False
    if(not('start_date' in request.POST and request.POST['start_date'])):
            return False
    if(not('end_date' in request.POST and request.POST['end_date'])):
            return False
    if(not('priority' in request.POST and request.POST['priority'])):
            return False
    if(not('duration' in request.POST and request.POST['duration'])):
            return False
    if(not('category' in request.POST and request.POST['category'])):
            return False
    return True