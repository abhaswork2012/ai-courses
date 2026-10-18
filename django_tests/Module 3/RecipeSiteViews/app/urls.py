from django.urls import path
from app import views
# Write your code here
urlpatterns = [
    path("", views.home, name="home"),
]
