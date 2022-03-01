from django.urls import path
from . import views

app_name = "djangoapp"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name='detail'),
    path('create/', views.create, name="create"),
    path('<int:question_id>/edit/', views.edit, name="edit"),
    path('<int:question_id>/delete/', views.delete, name="delete"),
]
