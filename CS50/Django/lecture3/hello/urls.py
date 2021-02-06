from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("voight", views.voight, name="voight"),
    path("pals", views.pals, name="pals")

]