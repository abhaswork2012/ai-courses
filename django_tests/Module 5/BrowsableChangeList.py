from django.contrib import admin
from app.models import Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """The product change list.
    Registered, so the pages exist - but nothing is configured, so the list
    is one column of ``__str__`` with no way to search, narrow or sort it.
    """
    # Write your code here