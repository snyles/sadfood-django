from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Item(models.Model):
  FINISH = (
    ('P', 'Just Plush'),
    ('K', 'Keychain'),
    ('O', 'Ornament'),
  )
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  materials = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  finish = models.CharField(
    max_length=1,
    choices=FINISH,
    default=FINISH[0][0]
  )
  categories = models.ManyToManyField(Category)

  def get_absolute_url(self):
    return reverse('item_detail', kwargs={'pk': self.id})

  def __str__(self):
      return self.name
  

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  favorites = models.ManyToManyField(Item)

  def __str__(self):
    return self.user.username
  

