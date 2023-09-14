from rest_framework import serializers

from content.models import Content


class ContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('material', 'educational_module')