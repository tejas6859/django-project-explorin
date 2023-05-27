from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=25)
    tag=models.CharField(max_length=25)
    SmallDesc= models.TextField()
    FullContent= models.TextField()
    Img= models.ImageField(upload_to='images/')

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name