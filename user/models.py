from django.db import models
from datetime import datetime
from django.contrib import admin

# Create your models here.

class Image(models.Model):
    image_path = models.CharField(max_length=250)
    exchange = models.CharField(max_length=250)
    symbol = models.CharField(max_length=250)

    def __str__(self):
        return (self.exchange+' '+self.symbol+' '+self.image_path)



class Visitor(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=250,unique=True)
    password = models.CharField(max_length=250)
    creation_time = models.CharField(max_length=250,default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    days = models.CharField(max_length=10,default=6)

    def __str__(self):
        return (self.name+' '+self.phone)


class VisitorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email', 'phone')