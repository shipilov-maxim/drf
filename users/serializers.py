from rest_framework import serializers

from users.models import Billing, User
from users.validators import StripePriceValidator


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'
        validators = [StripePriceValidator(field='payment_amount')]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
