from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="home"),
    path('shorten', views.short_url, name="shortUrl"),
    path('<str:hash_id>/', views.redirector, name="redirector")
]