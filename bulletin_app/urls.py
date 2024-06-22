from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('bulletin_app/<int:pk>/', views.post_detail, name='post_detail'),
    path('bulletin_app/new', views.post_create, name='post_create'),
    path('bulletin_app/<int:pk>/edit/', views.post_update, name='post_update'),
    path('bulletin_app/<int:pk>/delete/', views.post_delete, name='post_delete'),
]