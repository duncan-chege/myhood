from django.db import models
from django.contrib.auth.models import User

class Neighbourhood(models.Model):
    hood_name= models.CharField(max_length =50)
    hood_location= models.CharField(max_length =50)
    occupants= models.IntegerField(blank=True, null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):      #customize the way models are referenced in admin by adding this
        return self.hood_name

class Profile(models.Model):
    me = models.OneToOneField(User, on_delete=models.CASCADE)
    myhood = models.ForeignKey(Neighbourhood)
    profile_image = models.ImageField(default='default.jpeg')

    def __str__(self):
        return f"{self.me.username}'s Profile"

class Business(models.Model):
    person = models.ForeignKey(User)
    bizname = models.CharField(max_length =50)
    bizpost = models.CharField(max_length =500, blank=True, null=True)
    email= models.CharField(max_length =50)
    bizhood = models.ForeignKey(Neighbourhood)

    def __str__(self):
        return f"{self.person.username}'s Post"

    @classmethod
    def search_by_bizname(cls,bizname):
        searched = cls.objects.filter(bizname__icontains=bizname)
        return searched




