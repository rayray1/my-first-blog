from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# To make model visible on the admin page - register the model with;
admin.site.register(Post)


# Register model in admin panel
admin.site.register(Comment)