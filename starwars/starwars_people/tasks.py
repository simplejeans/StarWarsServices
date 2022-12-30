from celery import shared_task
from starwars_people.services import CSVDataWriterAndDBSaver


@shared_task()
def download_dataset():
    CSVDataWriterAndDBSaver().write_data_to_db_and_remove_from_disk()
