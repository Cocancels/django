from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:product_id>/', views.detail, name='detail'),
    path('create/', views.create, name="create"),
    path('<int:product_id>/edit/', views.edit, name="edit"),
    path('<int:product_id>/delete/', views.delete, name="delete"),
]
