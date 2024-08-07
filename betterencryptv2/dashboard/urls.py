from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.gen_view, name="dashboard")
]