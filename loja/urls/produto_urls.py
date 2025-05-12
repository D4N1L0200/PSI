from django.urls import path  # type: ignore
from loja.views.produto_view import list_produto_view

urlpatterns = [
    path("", list_produto_view, name="produtos"),
    path("<int:id>", list_produto_view, name="produto"),
]
