from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from app.models import Product
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
def search_products(name=None, min_price=None, max_price=None):
    # Write your code here
    raise NotImplementedError