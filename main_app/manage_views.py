from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Item, Category, Profile, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'sadfoodtoys'

def is_manager(user):
  return user.groups.filter(name='Manager').exists()

@user_passes_test(is_manager)
def add_photo(request, item_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, item_id=item_id)
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('item_list')


class ItemCreate(UserPassesTestMixin, CreateView):
  model = Item
  fields = '__all__'

  def test_func(self):
    return self.request.user.groups.filter(name='Manager').exists()

class ItemUpdate(UserPassesTestMixin, UpdateView):
  model = Item
  fields = '__all__'

  def test_func(self):
    return self.request.user.groups.filter(name='Manager').exists()

class ItemDelete(UserPassesTestMixin, DeleteView):
  model = Item
  success_url = '/items/'

  def test_func(self):
    return self.request.user.groups.filter(name='Manager').exists()

class ItemList(UserPassesTestMixin, ListView):
  model = Item

  def test_func(self):
    return self.request.user.groups.filter(name='Manager').exists()

class ItemDetails(UserPassesTestMixin, DetailView):
  model = Item

  def test_func(self):
    return self.request.user.groups.filter(name='Manager').exists()

class CategoryList(UserPassesTestMixin, ListView):
  model = Category

  def test_func(self):
    return self.request.user.groups.filter(name='Manager').exists()

class CategoryCreate(UserPassesTestMixin, CreateView):
  model = Category
  fields = '__all__'
  success_url = '/manage/category/list/'

  def test_func(self):
    return self.request.user.groups.filter(name='Manager').exists()

class CategoryUpdate(UserPassesTestMixin, UpdateView):
  model = Category
  fields = '__all__'
  success_url = '/manage/category/list/'

  def test_func(self):
    return self.request.user.groups.filter(name='Manager').exists()

class CategoryDelete(UserPassesTestMixin, DeleteView):
  model = Category
  success_url = '/manage/category/list/'

  def test_func(self):
    return self.request.user.groups.filter(name='Manager').exists()
