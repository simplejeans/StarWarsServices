from starwars_people.models import Dataset
from rest_framework import serializers


class DatasetSerializer(serializers.ModelSerializer):
    file_name = serializers.CharField(read_only=True)

    class Meta:
        model = Dataset
        fields = '__all__'
