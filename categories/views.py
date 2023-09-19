from django.shortcuts import render
from rest_framework import generics

from categories.models import Category
from categories.serializers import CategorySerializer
from educational_modules.models import EducationalModule


def index(request):
    """Вью для главной страницы"""

    return render(request, 'categories/index.html')


def about(request):
    """Вью для страницы about"""

    return render(request, 'categories/about.html')


def give_price(request):
    """Вью для страницы стоимость"""
    min_price = min([ed.price for ed in EducationalModule.objects.all()])
    return render(request, 'categories/price.html', {'min_price': min_price})


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
