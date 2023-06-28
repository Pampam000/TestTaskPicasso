import mimetypes
import time

from celery import shared_task

from project.settings import MIME_TYPE_TIMEOUTS, ANOTHER_MIME_TYPE_TIMEOUT
from .models import File


def get_mime_type_timeout(filename: str) -> int:
    mimetype = mimetypes.guess_type(filename)[0].split('/')[0]
    return MIME_TYPE_TIMEOUTS.get(mimetype, ANOTHER_MIME_TYPE_TIMEOUT)


@shared_task()
def save_file_task(file_id: int):
    """
    Imitation of a long synchronous file processing request
    """
    file = File.objects.get(id=file_id)
    timeout: int = get_mime_type_timeout(file.file.name)
    time.sleep(timeout)
    file.mark_as_processed()
