from rest_framework import serializers

from educational_modules.models import EducationalModule


class EducationalModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationalModule
        fields = ('name', 'description')
