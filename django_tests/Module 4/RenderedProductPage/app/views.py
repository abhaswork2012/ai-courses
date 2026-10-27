from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from app.models import Product
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
def product_page(request, pk):
    # Write your code here
    product = get_object_or_404(Product,pk=pk)
    return render(request,'app/product_detail.html',{"product":product})