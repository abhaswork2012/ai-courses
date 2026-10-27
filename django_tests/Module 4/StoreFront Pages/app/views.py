from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET
from app.models import Product
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
@require_GET
def product_list(request):
    # Write your code here
    raise NotImplementedError
@require_GET
def product_detail(request, pk):
    # Write your code here
    raise NotImplementedError