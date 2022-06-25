from django.apps import AppConfig
from django.apps import post


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
path("blog/", include("blog.urls", namespace="blog"))