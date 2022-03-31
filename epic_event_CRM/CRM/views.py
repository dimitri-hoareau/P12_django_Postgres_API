from rest_framework.viewsets import ModelViewSet
 
from CRM.models import Client, Contract, Event
from CRM.serializers import ClientSerializer, ContractSerializer, EventSerializer
 
class ClientViewSet(ModelViewSet):
 
    serializer_class = ClientSerializer
 
    def get_queryset(self):
        return Client.objects.all()

class ContractViewSet(ModelViewSet):
 
    serializer_class = ContractSerializer
 
    def get_queryset(self):
        return Contract.objects.all()

class EventViewSet(ModelViewSet):
 
    serializer_class = EventSerializer
 
    def get_queryset(self):
        return Event.objects.all()