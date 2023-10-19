from django.apps import AppConfig

class CustomPanelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_panel'

    def ready(self):
        from .models import create_view_permission
        # Connect the function to the post_migrate signal
        from django.db.models.signals import post_migrate
        post_migrate.connect(create_view_permission, sender=self)
