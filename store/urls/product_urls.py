from django.urls import path  # type: ignore
from django.shortcuts import redirect  # type: ignore
from store.views.product_view import product_view
from store.views.product_view import products_list_view

urlpatterns = [
    path("", products_list_view, name="products"),
    path("view/", lambda request: redirect("/product/")),
    path("view/<int:id>", product_view, name="product"),
]
