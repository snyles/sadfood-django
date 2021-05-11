from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='index'),
  # path('shop/', views.shop, name='shop'),
  path('category/<str:cat>/', views.category, name='category'),
  path('accounts/signup/', views.signup, name='signup'),

]