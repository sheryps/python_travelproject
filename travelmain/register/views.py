from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect



# Create your views here.
def loginn(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('loginn')
    return render(request,'login.html')

def register(request):
    if request.method =='POST':
        usernam=request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['cpassword']
        if password == cpass:
            if User.objects.filter(username=usernam).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=usernam,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save()
                return redirect('loginn')

        else:
            messages.info(request,'password not matching')
            return redirect('signup')
        return redirect('/')
    return render(request,'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
