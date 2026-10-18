# https://www.staffcoder.com/questions/safe-detail-and-json-views

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from app.models import Product
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
def product_detail(request, pk):
    # Write your code here
    product = get_object_or_404(Product, pk=pk)
    return render(request, "app/product_detail.html", {"product": product})
def product_json(request, pk):
    # Write your code here
    product = get_object_or_404(Product, pk=pk)
    return JsonResponse({
        "id": product.pk,
        "name": product.name,
        "description": product.description or "",
        "price": f"{product.price:.2f}",
    })
