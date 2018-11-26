from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from datetime import datetime,timedelta
from django.utils import timezone
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
                return HttpResponseRedirect(reverse('basic_app:profile'))
        else:
            return render(request,'basic_app/error.html',{'text':"Authentication failed."})

    else:
        return HttpResponseRedirect(reverse('index'))

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        books = models.catalogue.objects.filter(curr_user = user.username)
        student = models.userInfo.objects.get(user=user)
        name = student.user.first_name+' '+student.user.last_name
        semester = student.semester
        reg = student.register_number
        batch = student.batch
        fine = student.pending_fines
        return render(request,'basic_app/profileview.html',{'student_name':name,'semester':semester,'batch':batch,'reg':reg,'books_in_hand':len(books),'books':books,'fine':fine})
    else:
        return HttpResponseRedirect(reverse('index'))         
        
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def issueBook(request):
    if request.method == 'POST':
        try:
            book = request.POST.get('book')
            user = request.user
            
            query1 = models.catalogue.objects.get(book_id = book)
            if query1.issue_status == True:
                return render(request,'basic_app/error.html',{'text':"Please check the Book Id."})
            query1.curr_user = user.username
            query1.issue_status = True 
            query1.due_date = timezone.now()+timedelta(days = 14)
            query1.save()

            query2 = models.issueRegister(book = book,user = user.username,issue_time = timezone.now(),due_date = datetime.now()+timedelta(days = 14),return_time = datetime.now())
            query2.save()

            return HttpResponseRedirect(reverse('basic_app:profile'))
        except:
            return render(request,'basic_app/error.html',{'text':"Issue failed."})

    else:
        return render(request,'basic_app/error.html',{'text':"Issue failed."})

@login_required
def returnBook(request):

    if request.method == 'POST':
        book = request.POST.get('book')
        user = request.user
        try:
            issue = list(models.issueRegister.objects.filter(book = book,user = user.username).order_by('issue_time')).pop()
            issue.return_time = timezone.now()
            issue.returned = True
            issue.save()
        except:
            return render(request,'basic_app/error.html',{'text':"Blease check the book Id."})
        student = models.userInfo.objects.get(user=user)
        query1 = models.catalogue.objects.get(book_id = book)
        
        if (issue.return_time-issue.due_date).days > 14 :
            x = (issue.return_time-issue.due_date).days
            fine = 10 + ((x//10)*50)
            student.pending_fines += fine
            
        query1.curr_user = -1
        query1.issue_status = False
        query1.save()
        student.save()

        return HttpResponseRedirect(reverse('basic_app:profile'))
    else:
        return render(request,'basic_app/error.html',{'text':"Return failed."})

@login_required
def search(request):
    if request.method == "POST":
        query = request.POST.get('search')
        choice = request.POST.get('choice')
        if choice == "book":
            search_list = models.catalogue.objects.filter(book_title__icontains=query)
            print("hoi")
        elif choice == "author":
            search_list = models.catalogue.objects.filter(author__icontains=query)
        length = len(search_list)
        return render(request,'basic_app/results.html',{'length':length,'search_list':search_list}) 
    else:
        return render(request,'basic_app/error.html',{'text':"There was an error in one of the search parameters."})

@login_required
def search_form(request):
    return render(request,'basic_app/search.html')