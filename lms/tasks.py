from celery import shared_task
from lms.services import course_update_email
# import eventlet
#
#
# eventlet.monkey_patch()


@shared_task
def update_course(recipients, course_name):
    course_update_email(recipients, course_name)
