from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("toggle/<int:id>", views.toggle, name="toggle"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("new", views.new, name="new"),
]
