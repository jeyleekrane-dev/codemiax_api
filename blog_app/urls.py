from django.urls import path, include
from .import views
from rest_framework import routers


urlpatterns = [
    path('blogs/', views.BlogAll.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('blogs/comments/', views.BlogCommentView.as_view()),
    path('blogs/comments/<int:pk>', views.BlogCommentDetailView.as_view()),
    path('blogs/categories/', views.CategoriesView.as_view()),
    path('blogs/categories/<int:pk>', views.CategoriesDetailView.as_view())


]
