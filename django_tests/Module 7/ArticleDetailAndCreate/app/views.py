"""The request layer.
Two generic views, each missing what it cannot guess: the detail view needs
to know nothing more than its model, but the create view has no idea which
form to build or where to send the browser afterwards.
"""
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView
from app.models import Article
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
class ArticleDetailView(DetailView):
    model = Article
class ArticleCreateView(CreateView):
    model = Article
    # Write your code here