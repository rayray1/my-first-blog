from django.contrib import admin
from .models import Post

# Register your models here.

# to make model visible on the admin page - register the model with -;
admin.site.register(Post)
