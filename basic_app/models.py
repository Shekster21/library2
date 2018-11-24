from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class userInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    semester = models.IntegerField(default=1)
    batch = models.CharField(max_length = 1,default = 'A')
    register_number = models.CharField(max_length = 10,default = 'xxxx')
    pending_fines = models.IntegerField(default = 0)

    

    def __str__(self):
        return self.user.username

class catalogue(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_title = models.CharField(max_length = 150)
    author = models.CharField(max_length = 50)
    size = models.IntegerField()
    issue_status = models.BooleanField(default = False)
    due_date = models.DateTimeField(default = None)
    curr_user = models.IntegerField(default=None)




    def __str__(self):
        return self.book_title
    

class issueRegister(models.Model):

    issue_time = models.DateTimeField(default = None)
    book = models.IntegerField(default = None)
    user = models.IntegerField(default = None)
    due_date = models.DateTimeField(default = None)
    return_time = models.DateTimeField(default = None)
