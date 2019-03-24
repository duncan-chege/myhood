from django.db import models
from django.contrib.auth.models import User

class Neighbourhood(models.Model):
    hood_name= models.CharField(max_length =50)
    hood_location= models.CharField(max_length =50)
    occupants= models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):      #customize the way models are referenced in admin by adding this
        return self.hood_name

class Profile(models.Model):
    me = models.OneToOneField(User, on_delete=models.CASCADE)
    myhood = models.ForeignKey(Neighbourhood)
    profile_image = models.ImageField(default='default.jpeg')



