from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Item, Category, Profile

def is_manager(user):
  return user.groups.filter(name='Manager').exists()


# Create your views here.

def home(request):
  return render(request, 'home.html')

# @user_passes_test(is_manager)
# works for function views not class views
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

class ItemList(ListView):
  model = Item

class ItemDetails(DetailView):
  model = Item

class CategoryList(ListView):
  model = Category

class CategoryCreate(UserPassesTestMixin, CreateView):
  model = Category
  fields = '__all__'
  success_url = '/category/list/'

  def test_func(self):
    return self.request.user.groups.filter(name='Manager').exists()

class CategoryUpdate(UserPassesTestMixin, UpdateView):
  model = Category
  fields = '__all__'
  sucess_url = '/category/list'

  def test_func(self):
    return self.request.user.groups.filter(name='Manager').exists()

class CategoryDelete(UserPassesTestMixin, DeleteView):
  model = Category
  success_url = '/category/list/'

  def test_func(self):
    return self.request.user.groups.filter(name='Manager').exists()

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
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)