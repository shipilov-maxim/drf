from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

app_name = LmsConfig.name

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='create_lesson'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson'),
                  path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='update_lesson'),
                  path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='delete_lesson'),
              ] + router.urls
