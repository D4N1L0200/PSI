from django.contrib import admin  # type: ignore


from .models import Fabricante, Categoria, Produto

admin.site.register(Fabricante)
admin.site.register(Categoria)
admin.site.register(Produto)
