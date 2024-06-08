from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course
from users.models import User, Billing, Subscription
from users.serializers import BillingSerializer, UserSerializer
from users.services import create_price, create_session


class BillingListAPIView(generics.ListAPIView):
    serializer_class = BillingSerializer
    queryset = Billing.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('course', 'lesson', 'payment_method')
    ordering_fields = ('payday',)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        self.serializer_class = serializer.save()
        self.serializer_class.set_password(self.serializer_class.password)
        self.serializer_class.save()

    def perform_update(self, serializer):
        self.serializer_class = serializer.save()
        self.serializer_class.set_password(self.serializer_class.password)
        self.serializer_class.save()


class SubscriptionAPIView(APIView):

    def post(self, *args, **kwargs):
        course = get_object_or_404(Course, id=self.request.data.get('course'))
        subs_item = Subscription.objects.filter(course=course, user=self.request.user)
        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка отменена'
        else:
            Subscription.objects.create(user=self.request.user, course=course)
            message = 'Подписка оформлена'
        return Response({"message": message})


class BillingCreateAPIView(generics.CreateAPIView):
    serializer_class = BillingSerializer

    def perform_create(self, serializer):
        billing = serializer.save(user=self.request.user)
        if billing.course:
            name = billing.course.title
        elif billing.lesson:
            name = billing.lesson.title
        else:
            return Response({"message": 'Вы не указали курс либо урок'})
        price = create_price(billing.payment_amount, name)
        session_id, link = create_session(price)
        billing.session_id = session_id
        billing.link = link
        billing.save()
