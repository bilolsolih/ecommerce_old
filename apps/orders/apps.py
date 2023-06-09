from django.apps import AppConfig


class CartConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'apps.orders'

    def ready(self):
        import apps.orders.signals  # noqa
        # creates a cart model with one-to-one field to a user whenever a new user is created
