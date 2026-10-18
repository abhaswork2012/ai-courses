from django.urls import path
from app import views
# Write your code here
app_name = "blog"
urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.post_list,name='post-list'),
    path("posts/<int:year>/<slug:slug>/", views.post_detail,name='post-detail'),
    path("archive/<int:year>/", views.post_archive,name='post-archive'),
    path("blog/<int:pk>/", views.legacy_post_redirect),
]