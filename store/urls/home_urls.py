from django.urls import path  # type: ignore
from store.views.home_view import home_view

urlpatterns = [
    path("", home_view),
]
