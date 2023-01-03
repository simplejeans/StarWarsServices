from starwars_people.views import DatasetDetailView, TaskStatusApiView
from rest_framework.routers import SimpleRouter
from django.urls import path

router = SimpleRouter()
router.register(r'dataset', DatasetDetailView, basename='dataset')


urlpatterns = [
    path('task_status/', TaskStatusApiView.as_view(), )
]

urlpatterns += router.urls
