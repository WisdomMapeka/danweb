from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.home, name="home"),
    path('products/<slug>/', views.products, name="products"),
    path('tags/<slug>/', views.tags, name="tags"),
    path('client_message/', views.client_message, name="client_message")
]
