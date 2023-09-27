from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from content.models import Content
from content.serializers import ContentSerializers


class ContentDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'content/detail_content.html'

    def get(self, request, pk):
        content = get_object_or_404(Content, pk=pk)

        return Response({'content': content})


