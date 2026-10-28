from django.contrib import admin
from app.models import Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """The order page.
    Registered, so the page exists - but the items live on their own separate
    pages, the order total is nowhere, and marking a batch of orders shipped
    means opening every one of them.
    """
    list_display = ("reference", "status", "placed_on")
    # Write your code here