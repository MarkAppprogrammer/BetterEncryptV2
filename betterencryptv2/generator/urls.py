from django.urls import path

from . import views

urlpatterns = [
    path("generator/", views.gen_view, name="generator"),
    #path("result/", views.redirect_view, name="result")
]