from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from starwars_people.models import Dataset
from rest_framework import status, views
from starwars_people.serializers import DatasetSerializer
from starwars_people.services import make_pagination, start_download_dataset_task
from django.core.cache import cache


class DatasetDetailView(ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    @action(detail=False, methods=['post'])
    def download_dataset(self, request) -> Response:
        cache_task_key = start_download_dataset_task()
        return Response(cache_task_key, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        file_name = serializer.data["file_name"]
        response = make_pagination(file_name)
        return Response(response)


class TaskStatusApiView(views.APIView):

    def get(self, request, format=None):
        task_id = self.request.query_params['task_id']
        result = cache.get(task_id)
        return Response(result)




