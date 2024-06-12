from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Events(models.Model):
    name = models.CharField(verbose_name='Name of Event', max_length=100)
    pre_description = models.CharField(verbose_name='Pre description of Event', max_length=100)
    description = models.TextField(verbose_name='Description of Event')
    date = models.DateField(verbose_name='Date of Event')
    category = models.ForeignKey('Category',on_delete=models.PROTECT, verbose_name='Category', null=True)
    organization = models.ForeignKey('Organization',on_delete=models.PROTECT, verbose_name='Organization', null=True)
    level = models.ForeignKey('Level',on_delete=models.PROTECT, verbose_name='Level', null=True)
    photo = models.ImageField(verbose_name='Image of Event', upload_to='photo/%Y/%m/%d/', default='/photo/2024/04/06/empty.png')
    points = models.IntegerField(verbose_name='Points for event',null=True)
    
    def __str__(self):
        return self.name 
    
class Category(models.Model):
    name = models.CharField(verbose_name='Name of Category', max_length=60)
    
    def __str__(self):
        return self.name 
    
class Organization(models.Model):
    name = models.CharField(verbose_name='Name of Organization', max_length=60)
    
    
    def __str__(self):
        return self.name 
    
class Level(models.Model):
    name = models.CharField(verbose_name='Level of Event', max_length=60)        
    
    def __str__(self):
        return self.name 

class UserPoints(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username}'s Points: {self.points}"