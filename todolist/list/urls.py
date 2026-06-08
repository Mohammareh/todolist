from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/edit/", views.edit, name="edit"),
    path("<int:pk>/confirm_delete/", views.confirm_delete, name="confirm_delete"),
    path("<int:pk>/delete/", views.delete, name="delete"),

]