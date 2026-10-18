from django.urls import path
from app import views
# Write your code here
urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.post_list),
    path("posts/<int:year>/<slug:slug>/", views.post_detail),
    path("archive/<int:year>/", views.post_archive),
    path("blog/<int:pk>/", views.legacy_post_redirect),
]