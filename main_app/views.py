from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Item, Category, Profile

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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      profile = Profile(user=user)
      profile.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)