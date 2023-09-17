from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer

from categories.models import Category
from content.models import Content
from educational_modules.models import EducationalModule
from educational_modules.serializers import EducationalModuleSerializer, EdModuleWithContentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class EducationalModuleList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'educational_modules/list_educational_modules.html'

    def get(self, request):
        queryset_ed = EducationalModule.objects.all()
        return Response({'educational_modules': queryset_ed, 'categories': Category.objects.all()})

class EducationalModuleListFilter(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'educational_modules/list_educational_modules.html'

    def get(self, request, pk):
        if pk:
            queryset_ed = EducationalModule.objects.filter(category_id=pk)
            return Response({'educational_modules': queryset_ed, 'categories': Category.objects.all()})

class EducationalModuleLDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'educational_modules/educational_module.html'


    def get(self, request, pk):
        educational_module = get_object_or_404(EducationalModule, pk=pk)
        content = Content.objects.filter(educational_module__pk=educational_module.pk)

        return Response({'content': content, 'educational_module': educational_module})






class EducationalModuleListApiView(generics.ListAPIView):
    serializer_class = EducationalModuleSerializer
    queryset = EducationalModule.objects.all()



class EducationalModuleCreateApiView(generics.CreateAPIView):
    serializer_class = EducationalModuleSerializer
    queryset = EducationalModule.objects.all()


class EducationalModuleUpdateApiView(generics.UpdateAPIView):
    serializer_class = EducationalModuleSerializer
    queryset = EducationalModule.objects.all()


class EducationalModuleRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = EducationalModuleSerializer
    queryset = EducationalModule.objects.all()


class EducationalModuleDeleteApiView(generics.DestroyAPIView):
    serializer_class = EducationalModuleSerializer
    queryset = EducationalModule.objects.all()
