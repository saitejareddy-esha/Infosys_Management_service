from rest_framework import serializers
from .models import Dataset, DataElement

class DataElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataElement
        fields = '__all__'


class DatasetSerializer(serializers.ModelSerializer):
    elements = DataElementSerializer(many=True, read_only=True)

    class Meta:
        model = Dataset
        fields = '__all__'
