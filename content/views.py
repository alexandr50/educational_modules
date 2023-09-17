from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Content
from .serializers import ContentSerializers


class ContentDeatilView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'content/detail_content.html'

    def get(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        return Response({'content': content})


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
