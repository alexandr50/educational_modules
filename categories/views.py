from rest_framework import generics

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryListApiView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryCreateApiView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryUpdateApiView(generics.UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDeleteApiView(generics.DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


