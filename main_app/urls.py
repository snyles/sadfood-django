from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('item/create/', views.ItemCreate.as_view(), name='item_create'),
  path('item/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),
  path('item/<int:pk>/details', views.ItemDetails.as_view(), name='item_detail'),
  path('items', views.ItemList.as_view(), name='item_list'),
  
  
  
  
  path('category/create', views.CategoryCreate.as_view(), name='category_create'),
]