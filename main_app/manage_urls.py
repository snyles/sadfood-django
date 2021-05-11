from django.urls import path
from . import manage_views

urlpatterns = [

  path('items/', manage_views.ItemList.as_view(), name='item_list'),
  path('items/create/', manage_views.ItemCreate.as_view(), name='item_create'),
  path('items/<int:pk>/update/', manage_views.ItemUpdate.as_view(), name='item_update'),
  path('items/<int:pk>/delete/', manage_views.ItemDelete.as_view(), name='item_delete'),
  path('items/<int:pk>/details/', manage_views.ItemDetails.as_view(), name='item_detail'),
  path('category/list/', manage_views.CategoryList.as_view(), name='category_list'),
  path('category/create/', manage_views.CategoryCreate.as_view(), name='category_create'),
  path('category/<int:pk>/update/', manage_views.CategoryUpdate.as_view(), name='category_update'),
  path('category/<int:pk>/delete/', manage_views.CategoryDelete.as_view(), name='category_delete'),

]