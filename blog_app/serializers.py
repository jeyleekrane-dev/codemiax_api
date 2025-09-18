from rest_framework import serializers
from .models import Blog, Categories


class BlogSerializer (serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"


class CategorSerializer(serializers.ModelSerializer):
    # category = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = "__all__"


# class CategorSerializerLink(serializers.HyperlinkedModelSerializer):
#     category = BlogSerializer(many=True, read_only=True, view_name='cat-name')

#     class Meta:
#         model = Categories
#         fields = "__all__"
