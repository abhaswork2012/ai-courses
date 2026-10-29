"""The request layer.
Both views below fetch an article by the slug in the URL and then do as they
are told - which today means any signed-in visitor, and in fact any visitor
at all, can edit or delete anyone's work. Ownership has to be part of the
lookup, not an afterthought.
"""
from django.http import HttpResponse
from django.views.generic import DeleteView, UpdateView
from app.forms import ArticleForm
from app.models import Article
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    # Write your code here
class ArticleDeleteView(DeleteView):
    model = Article
    # Write your code here