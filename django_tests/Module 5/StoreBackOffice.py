from decimal import Decimal
from django.contrib import admin
from .models import Category, Product, Order, OrderItem
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "product_count")
    search_fields = ("name",)
    ordering = ("name",)
    @admin.display(description="Product count")
    def product_count(self, obj):
        return obj.products.count()
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "price",
        "tax_inclusive_price",
        "status",
        "added_on",
    )
    search_fields = ("name", "sku")
    list_filter = ("status", "added_on")
    ordering = ("-added_on", "name")
    @admin.display(description="Tax-inclusive price")
    def tax_inclusive_price(self, obj):
        return f"{obj.price * Decimal('1.2'):.2f}"
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 2
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("reference", "status", "placed_on", "total")
    search_fields = ("reference",)
    list_filter = ("status", "placed_on")
    ordering = ("-placed_on", "reference")
    inlines = (OrderItemInline,)
    readonly_fields = ("total",)
    actions = ("mark_shipped",)
    @admin.display(description="Total")
    def total(self, obj):
        if obj is None:
            return "0.00"
        total = sum(
            (item.quantity * item.unit_price for item in obj.items.all()),
            Decimal("0.00"),
        )
        return f"{total:.2f}"
    @admin.action(description="Mark selected orders as shipped")
    def mark_shipped(self, request, queryset):
        queryset.update(status="shipped")
