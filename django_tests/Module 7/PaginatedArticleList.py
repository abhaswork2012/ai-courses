"""The request layer.
``home`` is given. ``ArticleListView`` is a bare ``ListView``: it knows which
model to read and nothing else: not which template (and its default guess does
not exist), not what to call the list in the context, not how to order it, and
not that it should paginate at all.
"""
from django.http import HttpResponse
from django.views.generic import ListView
from app.models import Article
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
class ArticleListView(ListView):
    model = Article
    template_name = "app/articles.html"
    context_object_name = "articles"
    ordering = ("-published_on", "title")
    paginate_by = 5