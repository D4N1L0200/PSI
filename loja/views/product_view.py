from loja.models import Product
from django.utils import timezone  # type: ignore
from django.http import HttpResponse  # type: ignore
from django.shortcuts import render  # type: ignore
from datetime import timedelta, datetime


def id_input() -> str:
    return """
<form id="produtoForm">
    <label for="produto_id">ID do produto:</label>
    <input type="number" id="produto_id" name="id" min="0" step="1"/>
    <button type="submit">Buscar</button>
</form>

<script>
document.getElementById('produtoForm').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevent the default form submission
    const id = document.getElementById('produto_id').value;
    if (id) {
        window.location.href = '/produto/' + encodeURIComponent(id);
    }
});
</script>
"""


def get_product_card_template(product: Product) -> str:
    text: str = ""

    featured = "Yes" if product.featured else "No"
    sale = "Yes" if product.sale else "No"

    price: str = f"R${product.price:.2f}".replace(".", ",")
    image = product.image.url

    text += """
    <style>
        .product {
            display: flex;
            flex-direction: row;
            align-items: center;
            padding: 20px;
            border: 1px solid black;
            border-radius: 10px;
            margin-bottom: 20px;
            width: 100%;
        }

        .product h2, .product h3 {
            margin: 0 10px;
        }

        .product img {
            width: 150px;
            height: 150px;
            object-fit: cover;
            border-radius: 10px;
            margin-right: 10px;
        }

        .products {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
    </style>"""

    text += f"""
    <div class="products">
        <div class="product">
            <img src="{image}" alt="Produto">
            <div>
                <h2>Product: {product.name}</h2>
                <h3>Price: {price}</h3>
                <h3>Featured: {featured}</h3>
                <h3>Sale: {sale}</h3>
                <h3>Category: {product.category}</h3>
                <h3>Manufacturer: {product.manufacturer}</h3>
            </div>
        </div>
    </div>
    """

    return text


def products_list_view(request) -> HttpResponse:
    response_text: str = ""

    queries: dict[str, str | int] = {
        "name": "",
        "featured": "",
        "sale": "",
        "category": "",
        "manufacturer": "",
        "days": "",
    }

    product_list: list[Product] = []

    for query in queries.keys():
        if request.GET.get(query):
            queries[query] = request.GET.get(query)

    products = Product.objects.all()

    if any(queries.values()):

        if name_query := queries["name"]:
            products = products.filter(Produto__icontains=name_query)

        if featured_query := queries["featured"]:
            if isinstance(featured_query, str):
                products = products.filter(featured=featured_query.lower() == "true")

        if sale_query := queries["sale"]:
            if isinstance(sale_query, str):
                products = products.filter(sale=sale_query.lower() == "true")

        if category_query := queries["category"]:
            products = products.filter(category__Category__icontains=category_query)

        if manufacturer_query := queries["manufacturer"]:
            products = products.filter(
                manufacturer__Manufacturer__icontains=manufacturer_query
            )

        if days_query := queries["days"]:
            now = timezone.now()
            now = now - timedelta(days=int(days_query))
            products = products.filter(created_at__gte=now)

    for product in products:
        product_list.append(product)

    for product in product_list:
        product_template = get_product_card_template(product)
        response_text += product_template

    return HttpResponse(response_text)


def product_view(request, id: int) -> HttpResponse:
    produto = Product.objects.get(id=id)
    return render(request, "produto/view.html", {"produto": produto})
