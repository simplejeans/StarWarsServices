from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from starwars_people.models import Dataset
from starwars_people.serializers import DatasetSerializer
from starwars_people.services import CSVDataWriterAndDBSaver


class DatasetDetailView(ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    def create(self, request, *args, **kwargs):
        data = CSVDataWriterAndDBSaver()
        data.write_data_and_save_to_file()
        data.save_file_to_db_and_remove_from_disc()

        return Response(status=201)


