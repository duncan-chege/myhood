from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    url(r'^$',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    url(r'register/', views.register, name ='register'),
    url(r'^home',views.home, name='home'),
    url(r'profile/', views.profile, name='profile')
]