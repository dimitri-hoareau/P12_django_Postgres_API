from rest_framework.viewsets import ModelViewSet
 
from CRM.models import Client, Contract, Event
from CRM.serializers import ClientDetailSerializer, ClientListSerializer, ContractSerializer, EventSerializer
 
class ClientViewSet(ModelViewSet):
 
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
 
    def get_queryset(self):
        return Client.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

class ContractViewSet(ModelViewSet):
 
    serializer_class = ContractSerializer
 
    def get_queryset(self):
        return Contract.objects.all()

class EventViewSet(ModelViewSet):
 
    serializer_class = EventSerializer
 
    def get_queryset(self):
        return Event.objects.all()