from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from lms.models import Course, Lesson
from lms.paginators import PaginationClass
from lms.permissions import IsModer, IsOwner
from lms.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer
from lms.tasks import update_course


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = PaginationClass

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = (~IsModer,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action in ['destroy']:
            self.permission_classes = (~IsModer | IsOwner,)
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        self.serializer_class = serializer.save()
        self.serializer_class.owner = self.request.user
        self.serializer_class.save()

    def perform_update(self, serializer):
        course = serializer.save()
        recipients = [sub.user.email for sub in course.subscriptions.all()]
        update_course.delay(recipients, course.title)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (~IsModer, IsAuthenticated)

    def perform_create(self, serializer):
        self.serializer_class = serializer.save()
        self.serializer_class.owner = self.request.user
        self.serializer_class.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = PaginationClass


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
