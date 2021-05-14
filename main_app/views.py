from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Item, Category, Profile

def home(request):
  return render(request, 'home.html')

def shop(request):
  items = Item.objects.all()
  categories = Category.objects.all()
  return render(request, 'shop.html', {
    'items': items, 'catlist': categories})

class ItemDetail(DetailView):
  model = Item

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['catlist'] = Category.objects.all()
    return context

def category(request, cat):
  categories = Category.objects.all()
  cat_items = Item.objects.filter(categories__name__iexact=cat)
  return render(request, 'shop.html', {
    'category': cat, 'items': cat_items, 'catlist': categories})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      profile = Profile(user=user)
      profile.save()
      login(request, user)
      return redirect('shop')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)