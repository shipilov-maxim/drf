from datetime import timedelta

import stripe
from django.utils import timezone

from config.settings import STRIPE_API_KEY
from users.models import User

stripe.api_key = STRIPE_API_KEY


def create_price(amount, name):
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name": name},
    )


def create_session(price):
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")


def block_users():
    users = User.objects.exclude(last_login__isnull=True)
    now = timezone.now()
    for user in users:
        if now - user.last_login > timedelta(days=31):
            user.is_active = False
            user.save()
