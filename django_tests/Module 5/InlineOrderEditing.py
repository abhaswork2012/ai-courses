from django.contrib import admin
from app.models import Order, OrderItem
class OrderInLine(admin.TabularInline):
    model = OrderItem
    extra = 2
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """The order page.
    Registered, so the page exists - but the items live on their own separate
    pages, the order total is nowhere, and marking a batch of orders shipped
    means opening every one of them.
    """
    list_display = ("reference", "status", "placed_on")
    inlines = [OrderInLine]
    readonly_fields = ("total",)
    actions = ["mark_shipped"]
    @admin.display(description="Total Order")
    def total(self, obj):
        total = 0
        for item in obj.items.all():
            total += item.quantity * item.unit_price
        return f"{total}:2f"
    @admin.action(description="Mark selected invoices as paid")
    def mark_shipped(self, request, queryset):
        queryset.update(status=Order.SHIPPED)