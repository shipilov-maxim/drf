from django.contrib import admin

from users.models import User, Billing, Subscription


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'id', 'is_active')


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'lesson',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
