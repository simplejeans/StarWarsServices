from celery import shared_task
from starwars_people.adapters import StarWarsAdapters
from starwars_people.clients import StarWarsApiClient
from starwars_people.services import CSVDataWriterAndDBSaver, ImportStarwarsDataSet
from django.core.cache import cache


@shared_task()
def download_dataset_task(cache_task_id: str):
    try:
        cache.set(cache_task_id, {'is_importing': False, 'errors': []}, timeout=300)
        ImportStarwarsDataSet(client=StarWarsApiClient(), adapter=StarWarsAdapters(),
                              data_writer_service=CSVDataWriterAndDBSaver()).import_data()
    except Exception as exc:
        cache.set(cache_task_id, {'is_importing': False, 'errors': [exc.args]}, timeout=120)
    else:
        cache.set(cache_task_id, {'is_importing': True, 'errors': []}, timeout=120)