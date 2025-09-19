# from django.shortcuts import render
# from rest_framework import mixins, generics
# from .models import Blog, BlogComment, Categories
# from .serializers import BlogSerializer, CategorSerializer
# from rest_framework import viewsets
# from rest_framework.response import Response


# class FetchAllBlogs(generics.ListCreateAPIView):
#     queryset = Blog.objects.filter(is_public=False)
#     serializer_class = BlogSerializer

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = BlogSerializer(queryset, many=True)
#         if queryset.exists():
#             return Response({
#                 "status": True,
#                 "data": serializer.data
#             })
#         else:
#             return Response({
#                 "status": False,
#                 "data": "No data found"
#             })
#     def create(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = BlogSerializer()


# class SingleAndUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class CategoriesList(generics.ListAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategorSerializer


# class CategoriesDetails(generics.RetrieveAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategorSerializer


# # class CategorSerializerLink(generics.ListAPIView):
# #     queryset = Categories.objects.all()
# #     serializer_class = CategorSerializer

# class PowerMe (viewsets.ModelViewSet):
#     queryset = Blog.objects.filter(is_public=False)
#     serializer_class = BlogSerializer


from .serializers import BlogSerializer, BlogCommentSerializer, CategorSerializer
from .models import Blog, Categories, BlogComment
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny


class BlogAll(generics.ListCreateAPIView):
    queryset = Blog.objects.filter(is_public=False)
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogSerializer(queryset, many=True)
        if queryset.exists():
            return Response({
                "status": True,
                'serializer': serializer.data
            })
        else:
            return Response({
                "Status": False,
                "data": serializer.data
            })

    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogCommentView(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer


class BlogCommentDetailView (generics.RetrieveDestroyAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    lookup_field = 'pk'

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = BlogCommentSerializer(queryset, many=True)
    #     if queryset.exists():
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriesView (generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorSerializer(
            queryset, many=True, context={"request": request})
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriesDetailView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorSerializer
    lookup_field = "pk"
