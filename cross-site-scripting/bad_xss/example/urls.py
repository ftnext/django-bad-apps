from django.urls import path

from . import views

urlpatterns = [
    path("", views.example, name="example"),
    path("alert/", views.alert, name="alert"),
]
