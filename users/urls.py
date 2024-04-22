from django.urls import path
from users.apps import UsersConfig
from users.views import BillingListAPIView, MyTokenObtainPairView

app_name = UsersConfig.name

urlpatterns = [
    path('billing/', BillingListAPIView.as_view(), name='billings'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
