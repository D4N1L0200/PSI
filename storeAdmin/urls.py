"""
URL configuration for storeAdmin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore

from django.conf.urls.static import static  # type: ignore
from django.conf import settings  # type: ignore

from django.conf.urls import include  # type: ignore

from django.urls.resolvers import URLResolver, URLPattern  # type: ignore


urlpatterns: list[URLResolver | URLPattern] = [
    path("admin/", admin.site.urls),
    path("", include("store.urls.home_urls")),
    path("extra/", include("store.urls.extra_urls")),
    path("products/", include("store.urls.products_urls")),
]

urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns.extend(
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
)
