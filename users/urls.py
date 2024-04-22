from django.urls import path
from users.apps import UsersConfig
from users.views import BillingListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('billing/', BillingListAPIView.as_view(), name='billings'),
]
