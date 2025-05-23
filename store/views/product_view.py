from store.models import Product
from django.utils import timezone  # type: ignore
from django.http import HttpResponse  # type: ignore
from django.shortcuts import render  # type: ignore
from datetime import timedelta


def products_list_view(request):
    queries = {
        "name": "",
        "featured": "",
        "sale": "",
        "category": "",
        "manufacturer": "",
        "days": "",
    }

    products = Product.objects.all()

    for key in queries.keys():
        value = request.GET.get(key)
        if value:
            queries[key] = value

    if name_query := queries["name"]:
        products = products.filter(name__icontains=name_query)

    if featured_query := queries["featured"]:
        products = products.filter(featured=featured_query.lower() == "true")

    if sale_query := queries["sale"]:
        products = products.filter(sale=sale_query.lower() == "true")

    if category_query := queries["category"]:
        products = products.filter(category__name__icontains=category_query)

    if manufacturer_query := queries["manufacturer"]:
        products = products.filter(manufacturer__name__icontains=manufacturer_query)

    if days_query := queries["days"]:
        try:
            days = int(days_query)
            since = timezone.now() - timedelta(days=days)
            products = products.filter(created_at__gte=since)
        except ValueError:
            pass

    return render(
        request,
        "product/list.html",
        {"products": products},
    )


def product_view(request, id: int) -> HttpResponse:
    product = Product.objects.get(id=id)
    return render(request, "product/view.html", {"product": product})
