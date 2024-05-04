from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lms.models import Course, Lesson
from lms.validators import YoutubeURLValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YoutubeURLValidator(field='url_video')]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lesson_in_course = SerializerMethodField()
    lessons = LessonSerializer(many=True)
    is_subscribed = serializers.SerializerMethodField()

    def get_count_lesson_in_course(self, instance):
        return instance.lessons.count()

    def get_is_subscribed(self, instance):
        return instance.subscriptions.exists()

    class Meta:
        model = Course
        fields = '__all__'
