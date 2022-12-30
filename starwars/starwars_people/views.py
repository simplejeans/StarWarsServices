from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from starwars_people.models import Dataset
from rest_framework import status
from starwars_people.serializers import DatasetSerializer
from starwars_people.services import make_pagination
from starwars_people.tasks import download_dataset


class DatasetDetailView(ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    @action(detail=False, methods=['post'])
    def import_starwars_data(self, request):
        download_dataset()
        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        file_name = serializer.data["file_name"]
        response = make_pagination(file_name)
        return Response(response)
