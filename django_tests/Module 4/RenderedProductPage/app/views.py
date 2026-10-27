from django.http import HttpResponse
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
def product_page(request, pk):
    # Write your code here
    raise NotImplementedError