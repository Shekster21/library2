from django.urls import path,include,re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path(r'login/',views.user_login,name='login'),
    path(r'logout/',views.user_logout,name='logout'),
    path(r'issue/',views.issueBook,name='issue'),
    path(r'return/',views.returnBook,name='return'),
    path(r'profile/',views.profile,name = 'profile'),
    
    
]