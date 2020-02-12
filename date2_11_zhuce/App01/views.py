from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App01.forms import RegisterForm
from App01.models import User


def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')
            phone=form.cleaned_data.get('phone')
            user=User(username=username,password=password,email=email,phone=phone)
            print(username,password,email,phone)
            user.save()
            return HttpResponse('首页')
        else:
            return render(request,'register.html',locals())

    return render(request,'register.html')