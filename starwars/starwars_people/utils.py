from datetime import datetime
import uuid


def create_file_name():
    file_name = datetime.now().strftime('%b.%d.%Y_%I.%M%p')
    return file_name


def generate_cache_task_key():
    return str(uuid.uuid1())
