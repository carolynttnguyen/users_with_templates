from django.shortcuts import render, redirect
from .models import users

def index(request): 
    context = {
        "all_users": users.objects.all()
    }
    return render(request, "index.html", context)

def add_user(request):
    users.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        age=request.POST['age']
    )
    return redirect('/')