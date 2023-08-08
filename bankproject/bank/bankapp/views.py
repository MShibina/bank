from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    return render(request,'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('bankapp:form')
        else:
            context = {
                'error':True,
                'message':'Invalid Credentials'
            }
            return render(request,'login.html',context)
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                context ={
                    'error' :True,
                    'message': 'Username Already exists'
                }
                return render(request,'register.html',context)
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('bankapp:login')
        else:
            context={
                'error':True,
                'message':'Password not matching'
            }
            return render(request,'register.html',context)
        return redirect('/')
    return render(request,'register.html')
def form(request):
    return render(request,'form.html')
def application(request):
    return render(request,'application.html')
def logout(request):
    auth.logout(request)
    return redirect('bankapp:home')


