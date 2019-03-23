from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    url('^$',views.home, name = 'home'),
    url('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    url('register/', views.register, name ='register'),
    url('profile/', views.profile, name='profile')
]