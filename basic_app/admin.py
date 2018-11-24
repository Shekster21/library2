from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from basic_app import models

class catalogueAdmin(admin.ModelAdmin):
    list_display = ['book_id','book_title','author','issue_status','due_date','curr_user']
    ordering = ['book_id']
    search_fields = ['book_id','book_title','author','curr_user']


class userInfoAdmin(admin.ModelAdmin):
    list_display = ['user','semester','batch','pending_fines']
    ordering = ['user']
    search_fields = ['user','semester','batch']

class registerAdmin(admin.ModelAdmin):
    list_display = ['book','user','issue_time','due_date','returned']
    ordering = ['issue_time']
    search_fields = ['book','user']

admin.site.register(models.userInfo,userInfoAdmin) 
admin.site.register(models.catalogue,catalogueAdmin)
admin.site.register(models.issueRegister,registerAdmin)