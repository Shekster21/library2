from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from datetime import datetime
from basic_app import models

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

def login_form(request):
    return render(request,'basic_app/login.html')

def issue_form(request):
    return render(request,'basic_app/issue.html')

def return_form(request):
    return render(request,'basic_app/return.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                books = models.catalogue.objects.filter(curr_user = user.username)
                student = models.userInfo.objects.get(user=user)
                name = student.user.first_name+' '+student.user.last_name
                semester = student.semester
                reg = student.register_number
                batch = student.batch
                return render(request,'basic_app/profileview.html',{'student_name':name,'semester':semester,'batch':batch,'reg':reg,'books_in_hand':len(books),'books':books})
        else:
            return render(request,'basic_app/error.html',{'text':"Authentication failed."})

    else:
        return
        
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def issueBook(request):
    if request.method == 'POST':
        book = request.POST.get('book')
        user = request.POST.get('user')
        
        query1 = models.catalogue.objects.get(book_id = book)
        query1.curr_user = user
        query1.issue_status = True 
        query1.save()

        query2 = models.issueRegister(book = book,user = user,issue_time = datetime.now(),return_time = datetime.now())
        query2.save()

        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,'basic_app/error.html',{'text':"Issue failed."})

@login_required
def returnBook(request):

    if request.method == 'POST':
        book = request.POST.get('book')
        user = request.POST.get('user')

        issue = list(models.issueRegister.objects.filter(book = book,user = user).order_by('issue_time')).pop()
        issue.return_time = datetime.now()
        issue.save()

        query1 = models.catalogue.objects.get(book_id = book)
        query1.curr_user = -1
        query1.issue_status = False
        query1.save()

        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,'basic_app/error.html',{'text':"Return failed."})