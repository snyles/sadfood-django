from django.contrib import admin
from .models import Profile, Category, Item, Photo

# Register your models here.

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Photo)