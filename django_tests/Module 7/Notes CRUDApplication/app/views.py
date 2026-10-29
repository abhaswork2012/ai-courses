"""The request layer.
Five generic views, each declared with its model and nothing else. None of
them is gated, none of them is scoped to the signed-in owner, the list does
not paginate, the create view has no form and no owner to attach, and the
delete view has nowhere to go afterwards.
"""
from app.forms import NoteForm
from django.http import HttpResponse
from django.urls import reverse_lazy,reverse
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import Note
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
class NoteListView(LoginRequiredMixin,ListView):
    model = Note
    template_name = "app/notes.html"
    context_object_name = "notes"
    paginate_by = 5
    def get_queryset(self):
        return super().get_queryset().filter(
            owner=self.request.user
        ).order_by("-created_on", "-pk")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["note_total"] = Note.objects.filter(
            owner=self.request.user
        ).count()
        return context
class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "app/note_detail.html"
    context_object_name = "note"
    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)
class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Note
    template_name = "app/note_form.html"
    form_class = NoteForm
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
class NoteUpdateView(LoginRequiredMixin,UpdateView):
    model = Note
    template_name = "app/note_form.html"
    form_class = NoteForm
    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)
    
    def get_success_url(self) -> str:
        return reverse("note-detail", kwargs={"slug": self.object.slug})
class NoteDeleteView(LoginRequiredMixin,DeleteView):
    model = Note
    template_name = "app/note_confirm_delete.html"
    success_url = reverse_lazy("note-list")
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)