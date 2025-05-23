from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.db.models.signals import post_save  # type: ignore
from django.dispatch import receiver  # type: ignore

from .manufacturer import Manufacturer
from .category import Category
from .product import Product
