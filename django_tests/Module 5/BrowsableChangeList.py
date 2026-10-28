from django.contrib import admin
from decimal import Decimal
from app.models import Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """The product change list.
    Registered, so the pages exist - but nothing is configured, so the list
    is one column of ``__str__`` with no way to search, narrow or sort it.
    """
    # Write your code here
    list_display = ("name", "sku", "price", "tax_inclusive_price", "status", "added_on")
    search_fields = ("name", "sku")
    list_filter = ('status','added_on')
    ordering = ('-added_on','name')
    @admin.display(description="Price incl. tax")
    def tax_inclusive_price(self, obj):
        return f"{obj.price * Decimal("1.2"):.2f}"