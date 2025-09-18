from django.urls import path
from .import views

urlpatterns = [
    path('blogs/', views.FetchAllBlogs.as_view(), name='blogs_list'),
    path('blogs/<int:pk>', views.SingleAndUpdate.as_view()),
    path('categories/', views.CategoriesList.as_view()),
    path('categories/<int:pk>', views.CategoriesDetails.as_view()),
    # path('cat/', views. CategorSerializerLink.as_view(), name= 'cat-name')
]
