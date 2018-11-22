from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

def login_form(request):
    return render(request,'basic_app/login.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,'basic_app/profileview.html',{'firstname':user.first_name,'lastname':user.last_name})
        else:
            return render(request,'basic_app/error.html',{'text':"Authentication failed."})

    else:
        return
        
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
