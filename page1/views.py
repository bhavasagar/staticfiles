from django.shortcuts import redirect, render
from django.http import request
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import login, logout
# from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request,template_name='mainpage/index.html')

def about(request):
    return render(request,template_name='includes/about.html')

def contact(request):
    return render(request,template_name='includes/contact.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirmpassword']
        if password==cpassword and (len(password)>6 and len(password)<15):
            if User.objects.filter(email=email).exists():
                messages.info(request,'email is taken')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.info(request,f"Logged in as {user.username}")
                login(request,user)
                return redirect('/')
        else:
            messages.info(request,'passwords are not matching')
    return render(request,
                    template_name='includes/register.html')

def loginto(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # messages.info(request,"working")
        user1 = auth.authenticate(username=username,password=password)
        if user1 is not None:
            login(request,user1)
            messages.info(request,f"Logged in as {user1.username}")
            return redirect('/')
        else:
            return redirect('/register')
            messages.info(request,"Pocess failed...Unable to login")
    return render(request,
                    template_name='includes/login.html')

def logoutof(request):
    logout(request)
    messages.info(request,"Logged out successfully")
    return redirect("homepage:homepage")