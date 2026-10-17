from decimal import Decimal
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from django.db.models import Q
from app.models import Product

def search_products(name=None, min_price=None, max_price=None):
    # Write your code here
    products = Product.objects.filter(is_active=True)
    if name:
        products = products.filter(Q(name__icontains=name))
    if min_price is not None:
        min_price = Decimal(min_price)
        products = products.filter(Q(price__gte=min_price))
    if max_price is not None:
        max_price = Decimal(max_price)
        products = products.filter(Q(price__lte=max_price))
    
    products = products.order_by('price','name')
    return products
@require_GET
def product_search(request):
    products = search_products(
        name=request.GET.get("name") or None,
        min_price=request.GET.get("min_price") or None,
        max_price=request.GET.get("max_price") or None,
    )
    results = [
        {
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "is_active": product.is_active,
        }
        for product in products
    ]
    return JsonResponse({"count": len(results), "results": results})