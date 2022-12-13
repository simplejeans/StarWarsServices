
from starwars_people.views import DatasetDetailView

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'dataset', DatasetDetailView, basename='dataset')

urlpatterns = []

urlpatterns += router.urls
