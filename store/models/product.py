from store.models import *


class Product(models.Model):
    name = models.CharField(null=False, max_length=100)
    featured = models.BooleanField(default=True)
    sale = models.BooleanField(default=True)
    sale_msg = models.CharField(null=True, max_length=100, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category, null=True, related_name="category", on_delete=models.SET_NULL
    )
    manufacturer = models.ForeignKey(
        Manufacturer, null=True, related_name="manufacturer", on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    altered_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
