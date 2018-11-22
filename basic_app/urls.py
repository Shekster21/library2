from django.urls import path,include,re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    re_path(r'^login/$',views.user_login,name='login'),
    re_path(r'^logout/$',views.user_logout,name='logout'),
    
    
]