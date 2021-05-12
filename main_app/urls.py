from django.urls import path, include
from . import views

urlpatterns = [
  # path('', views.home, name='home'),
  path('', views.shop, name='shop'),
  # path('about/', views.about, name='about'),
  path('category/<str:cat>/', views.category, name='category'),
  path('item/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
  path('manage/', include('main_app.manage_urls')),
  path('accounts/signup/', views.signup, name='signup'),
]