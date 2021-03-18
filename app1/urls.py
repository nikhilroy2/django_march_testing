from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="home"),
    path('edit/<str:pk>', views.edit, name="edit"),
    path('delete/<str:pk>', views.delete, name="delete")
]