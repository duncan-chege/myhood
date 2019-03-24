from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    url(r'register/', views.register, name ='register'),
    url(r'^home',views.home, name='home'),
    url(r'^enter-hood/',views.hood_details, name='hood_details'),
    url(r'^profile/(\d+)', views.profile, name='profile')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)