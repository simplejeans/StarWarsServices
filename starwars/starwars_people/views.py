from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from starwars_people.models import Dataset
from starwars_people.serializers import DatasetSerializer
from starwars_people.services import make_pagination
from starwars_people.tasks import download_dataset


class DatasetDetailView(ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    def create(self, request, *args, **kwargs):
        download_dataset()
        return Response(status=201)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        file_name = serializer.data["file_name"]
        response = make_pagination(file_name)
        return Response(response)
