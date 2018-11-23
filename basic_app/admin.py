from django.contrib import admin

# Register your models here.
from basic_app import models

admin.site.register(models.userInfo) 
admin.site.register(models.catalogue)
admin.site.register(models.issueRegister)