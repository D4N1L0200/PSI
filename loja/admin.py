from django.contrib import admin  # type: ignore
from .models import Fabricante, Categoria, Produto


class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = "criado_em"


class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = "criado_em"
    list_display = (
        "Produto",
        "destaque",
        "promocao",
        "msgPromocao",
        "preco",
        "categoria",
    )
    search_fields = ("Produto",)
    exclude = ("msgPromocao",)
    empty_value_display = "Vazio"


admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
