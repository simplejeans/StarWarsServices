from celery import shared_task
from starwars_people.services import CSVDataWriterAndDBSaver
from django.core.cache import cache


@shared_task()
def download_dataset_task(cache_task_id: str):
    try:
        cache.set(cache_task_id, {'is_importing': False, 'errors': []}, timeout=300)
        CSVDataWriterAndDBSaver().write_data_to_db_and_remove_from_disk()
    except Exception as exc:
        cache.set(cache_task_id, {'is_importing': False, 'errors': [exc.args]}, timeout=120)
    else:
        cache.set(cache_task_id, {'is_importing': True, 'errors': []}, timeout=120)
