from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from content.models import Content
from educational_modules.models import EducationalModule


class EducationalModuleSerializer(serializers.ModelSerializer):
    content = SerializerMethodField()

    def get_content(self, education_module):
        queryset = [con.name for con in Content.objects.filter(educational_module=education_module)]
        return queryset
    class Meta:
        model = EducationalModule
        fields = ('name', 'description', 'price', 'image', 'content')



