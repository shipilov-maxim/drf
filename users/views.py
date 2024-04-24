from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User, Billing
from users.serializers import BillingSerializer, UserSerializer


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
