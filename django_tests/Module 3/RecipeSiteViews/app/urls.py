from django.urls import path,register_converter
from app import views
# Write your code here
app_name = "recipes"
class YearConverter:
    regex = r"[1-9][0-9]{3}"
    def to_python(self, value):
        return int(value)
    def to_url(self, value):
        return str(value)
register_converter(YearConverter, "year")
urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/", views.recipe_list, name="recipe-list"),
    path("recipes/archive/<year:year>/", views.recipe_archive, name="recipe-archive"),
    path("recipe/<int:pk>/", views.legacy_recipe_redirect, name="legacy-recipe"),
    path("recipes/<slug:slug>/", views.recipe_detail, name="recipe-detail"),
    path("api/recipes/<slug:slug>/", views.recipe_json, name="recipe-json"),
]