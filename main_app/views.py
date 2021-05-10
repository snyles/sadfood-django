from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Item, Category

# Create your views here.

def home(request):
  return render(request, 'home.html')

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemUpdate(UpdateView):
  model = Item
  fields = '__all__'

class ItemList(ListView):
  model = Item

class ItemDetails(DetailView):
  model = Item

class CategoryList(ListView):
  model = Category

class CategoryCreate(CreateView):
  model = Category
  fields = '__all__'
  success_url = '/category/list/'

class CategoryUpdate(UpdateView):
  model = Category
  fields = '__all__'
  sucess_url = '/category/list'

class CategoryDelete(DeleteView):
  model = Category
  success_url = '/category/list/'