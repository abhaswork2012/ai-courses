from django.http import HttpResponse, JsonResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from app.models import Recipe
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "app/recipe_list.html", {"recipes": recipes})
def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, "app/recipe_detail.html", {"recipe": recipe})
def recipe_archive(request, year):
    recipes = Recipe.objects.filter(year=year)
    return render(request, "app/recipe_archive.html", {
        "recipes": recipes,
        "year": year,
    })
def recipe_json(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return JsonResponse({
        "id": recipe.pk,
        "title": recipe.title,
        "slug": recipe.slug,
        "description": recipe.description or "",
        "year": recipe.year,
        "url": reverse("recipes:recipe-detail", args=[recipe.slug]),
    })
def legacy_recipe_redirect(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    url = reverse("recipes:recipe-detail", args=[recipe.slug])
    return HttpResponsePermanentRedirect(url)