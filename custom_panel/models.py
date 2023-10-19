from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_migrate
from landingpage.models import ClientData  # Import the ClientData model

# Model definitions

def create_view_permission(sender, **kwargs):
    content_type = ContentType.objects.get_for_model(ClientData)

    # Check if the permission already exists
    view_permission, created = Permission.objects.get_or_create(
        codename='view_clientdata',
        content_type=content_type,
        defaults={'name': 'Can view ClientData'}
    )

    # Update the name if the permission already exists
    if not created and view_permission.name != 'Can view ClientData':
        view_permission.name = 'Can view ClientData'
        view_permission.save()

# Connect the function to the post_migrate signal
post_migrate.connect(create_view_permission, sender=models)
