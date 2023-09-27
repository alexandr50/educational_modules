from rest_framework import generics

from educational_modules.models import EducationalModule
from educational_modules.serializers import EducationalModuleSerializer


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
