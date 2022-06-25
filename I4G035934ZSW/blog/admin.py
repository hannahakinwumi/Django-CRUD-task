from django.contrib import admin

# Register your models here.
from .models import Blog
admin.site.register(Blog)
from .models import post
admin.site.register(post)