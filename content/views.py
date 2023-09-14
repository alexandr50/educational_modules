from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Content
from .serializers import ContentSerializers


class ContentListApiView(generics.ListAPIView):
    serializer_class = ContentSerializers
    queryset = Content.objects.all()


class ContentCreateApiView(generics.CreateAPIView):
    serializer_class = ContentSerializers
    queryset = Content.objects.all()


class ContentUpdateApiView(generics.UpdateAPIView):
    serializer_class = ContentSerializers
    queryset = Content.objects.all()


class ContentRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ContentSerializers
    queryset = Content.objects.all()


class ContentDeleteApiView(generics.DestroyAPIView):
    serializer_class = ContentSerializers
    queryset = Content.objects.all()
