from celery import shared_task
import eventlet


eventlet.monkey_patch()


@shared_task
def add_numbers():
    return 'A'
