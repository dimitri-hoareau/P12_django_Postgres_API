from rest_framework.serializers import ModelSerializer
 
from CRM.models import Client, Contract, Event
 
class ClientDetailSerializer(ModelSerializer):
 
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created', 'date_updated']

class ClientListSerializer(ModelSerializer):
 
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email','company_name']

class ContractSerializer(ModelSerializer):
 
    class Meta:
        model = Contract
        fields = ['id', 'name', 'status', 'amount', 'payment_due', 'date_created', 'date_updated']

class EventSerializer(ModelSerializer):
 
    class Meta:
        model = Event
        fields = ['id', 'name', 'attendees', 'event_date', 'notes', 'date_created', 'date_updated']