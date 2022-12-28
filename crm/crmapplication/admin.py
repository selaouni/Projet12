from django.contrib import admin

from crmapplication.models import Client
from crmapplication.models import Contract
from crmapplication.models import Event
from crmapplication.models import Sales
from crmapplication.models import Support

# Register your models here.

admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
admin.site.register(Sales)
admin.site.register(Support)

