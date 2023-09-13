from .models import CustomUser
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
