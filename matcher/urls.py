from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("history/", views.history, name="history"),
    path("history/<int:pk>/", views.detail, name="detail"),
    path("history/<int:pk>/delete/", views.delete_analysis, name="delete"),
]