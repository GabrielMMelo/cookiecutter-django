from django.contrib.auth import get_user_model
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404
)

@login_required
def home(request):
   return render(request, 'core/home.html', context={}) 

