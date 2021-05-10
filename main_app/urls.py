from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('items/create/', views.ItemCreate.as_view(), name='item_create'),
  path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),
  path('items/<int:pk>/details/', views.ItemDetails.as_view(), name='item_detail'),
  path('items/', views.ItemList.as_view(), name='item_list'),
  
  
  path('category/list/', views.CategoryList.as_view(), name='category_list'),
  path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
  path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
  path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),


]