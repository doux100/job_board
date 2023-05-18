from rest_framework import serializers
from .models import job


class jobserializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = '__all__'
