from django.contrib import admin

from .models import Client
from .models import Contract
from .models import Event
from .models import Sales
from .models import Support
from .models import Event_status


class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'first_name', 'last_name', 'email', 'company_name', 'sales_contact')
    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'client', 'Support_contact', 'event_status', 'notes')
    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True


class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_id', 'sales_contact', 'client', 'status', 'payment_due')
    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True


class SupportAdmin(admin.ModelAdmin):
    list_display = ('support_id', 'contact','first_name', 'last_name')
    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True


class SalesAdmin(admin.ModelAdmin):
    list_display = ('sales_id', 'contact', 'first_name', 'last_name')
    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True



admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Support, SupportAdmin)
admin.site.register(Event_status)

