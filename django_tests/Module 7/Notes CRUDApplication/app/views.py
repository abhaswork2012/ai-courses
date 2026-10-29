"""The request layer.
Five generic views, each declared with its model and nothing else. None of
them is gated, none of them is scoped to the signed-in owner, the list does
not paginate, the create view has no form and no owner to attach, and the
delete view has nowhere to go afterwards.
"""
from django.http import HttpResponse
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView,
)
from app.models import Note
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
class NoteListView(ListView):
    model = Note
    # Write your code here
class NoteDetailView(DetailView):
    model = Note
    # Write your code here
class NoteCreateView(CreateView):
    model = Note
    # Write your code here
class NoteUpdateView(UpdateView):
    model = Note
    # Write your code here
class NoteDeleteView(DeleteView):
    model = Note
    # Write your code here