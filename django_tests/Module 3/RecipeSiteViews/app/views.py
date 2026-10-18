from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from app.models import Recipe
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
def recipe_list(request):
    # Write your code here
    raise NotImplementedError
def recipe_detail(request, slug):
    # Write your code here
    raise NotImplementedError
def recipe_archive(request, year):
    # Write your code here
    raise NotImplementedError