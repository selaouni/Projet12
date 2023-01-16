from rest_framework.serializers import ModelSerializer
from .models import Client, Event, Contract, Event_status, Sales, Support
import logging

logger = logging.getLogger(__name__)


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s',
                    )

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'first_name',
                  'last_name', 'email',
                  'phone', 'mobile', 'company_name',
                  'date_created', 'date_updated',
                  'sales_contact']


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_id', 'client','support_contact',
                  'date_created', 'date_updated','event_status',
                  'attendees','event_date','notes']


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['contract_id', 'sales_contact',
                  'client', 'date_created', 'date_updated',
                  'status', 'amount',
                  'payment_due']


class EventStatusSerializer(ModelSerializer):
    class Meta:
        model = Event_status
        fields = ['event_status_id', 'Event_status']


class SalesSerializer(ModelSerializer):
    class Meta:
        model = Sales
        fields = ['sales_id', 'contact', 'first_name', 'last_name']


class SupportSerializer(ModelSerializer):
    class Meta:
        model = Support
        fields = ['support_id', 'contact', 'first_name', 'last_name']