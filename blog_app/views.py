from django.shortcuts import render
from rest_framework import mixins, generics
from .models import Blog, BlogComment, Categories
from .serializers import BlogSerializer, CategorSerializer


class FetchAllBlogs(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class SingleAndUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CategoriesList(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorSerializer


class CategoriesDetails(generics.RetrieveAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorSerializer


# class CategorSerializerLink(generics.ListAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategorSerializer
