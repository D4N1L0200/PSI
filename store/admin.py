from django.contrib import admin  # type: ignore
from .models import Manufacturer, Category, Product


class ManufacturerAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"


class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = (
        "name",
        "featured",
        "sale",
        "sale_msg",
        "price",
        "category",
    )
    search_fields = ("Product",)
    exclude = ("sale_msg",)
    empty_value_display = "Empty"


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
