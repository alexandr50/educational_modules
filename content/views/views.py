from django.shortcuts import get_object_or_404
from rest_framework import generics

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from content.models import Content
from content.serializers import ContentSerializers


class ContentDetailView(DetailView):
    model = Content
    template_name = 'content/detail_content.html'
    extra_context = {
        'title': 'Материал'
    }

    def get_object(self, queryset=None):
        return Content.objects.get(id=self.kwargs['pk'])



