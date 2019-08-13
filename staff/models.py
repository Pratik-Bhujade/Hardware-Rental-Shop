# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Tool(models.Model):
    tooltype = models.IntegerField()
    name = models.CharField(max_length=50,unique=True)
    quantity = models.IntegerField()
    daycost = models.DecimalField(max_digits=10,decimal_places=2)
    weekcost = models.DecimalField(max_digits=10,decimal_places=2)
    monthcost = models.DecimalField(max_digits=10,decimal_places=2)

class Cart(models.Model):
    cost = models.DecimalField(max_digits=15,decimal_places=2)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    payment = models.CharField(max_length=20)
    phonenumber = PhoneNumberField('phone number')

class Entry(models.Model):
    item = models.ForeignKey(Tool)
    cart = models.ForeignKey(Cart,null = True)
    dwm = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=20,decimal_places=2)
