from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from app.models import Product
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
def product_detail(request, pk):
    # Write your code here
    raise NotImplementedError
def product_json(request, pk):
    # Write your code here
    raise NotImplementedError