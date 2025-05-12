from django.urls import path  # type: ignore
from loja.views.extra_views import emoji_view, snake_view, about_view

urlpatterns = [
    path("emoji/", emoji_view),
    path("snake/", snake_view),
    path("about/", about_view),
]
