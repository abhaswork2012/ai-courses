from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from app.models import Post
def home(request):
    return HttpResponse(f"Backend server running on port {request.get_port()}")
def post_list(request):
    return render(request, "app/post_list.html", {"posts": Post.objects.all()})
def post_detail(request, year, slug):
    post = get_object_or_404(Post, year=year, slug=slug)
    return render(request, "app/post_detail.html", {"post": post})
def post_archive(request, year):
    posts = Post.objects.filter(year=year)
    return render(request, "app/post_archive.html", {"year": year, "posts": posts})
def legacy_post_redirect(request, pk):
    # Write your code here
    raise NotImplementedError
