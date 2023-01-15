import os
import django
from django.contrib.auth.models import Group


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_permission.settings')
django.setup()


GROUPS = ['IsAdmin', 'IsSupport', 'IsSales']
MODELS = ['Support', 'Sales']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)
