"""The request layer.
Both views below fetch an article by the slug in the URL and then do as they
are told - which today means any signed-in visitor, and in fact any visitor
at all, can edit or delete anyone's work. Ownership has to be part of the
lookup, not an afterthought.
"""
from django.http import HttpResponse
from django.views.generic import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView
from app.forms import ArticleForm
from app.models import Article
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "app/article_form.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)
    def get_success_url(self):
        return reverse("article-detail", kwargs={"slug": self.object.slug})
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "app/article_confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("article-list")
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)