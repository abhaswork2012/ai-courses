from django.urls import path,register_converter
from app import views
# Write your code here
class YearConverter:
    regex = r'[1-9][0-9]{3}'
    def to_python(self, value):
        return int(value)
    def to_url(self, value):
        return str(value)
register_converter(YearConverter, 'year')
urlpatterns = [
    path("", views.home, name="home"),
    path("articles/<int:article_id>/", views.article_detail, name="article-detail"),
    path("articles/by-slug/<slug:slug>/", views.article_by_slug, name="article-by-slug"),    
    path("articles/archive/<year:year>/", views.article_archive, name="article-archive")
]