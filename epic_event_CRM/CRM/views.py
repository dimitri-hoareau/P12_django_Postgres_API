from rest_framework.viewsets import ModelViewSet
 
from CRM.models import Client, Contract, Event, SalesStaff, GestionStaff, SupportStaff
from CRM.serializers import ClientSerializer, ContractSerializer, EventSerializer, SalesStaffSerializer, GestionStaffSerializer, SupportStaffSerializer

class GestionStaffViewSet (ModelViewSet):
 
    serializer_class = GestionStaffSerializer
 
    def get_queryset(self):
        return GestionStaff.objects.all()

class SupportStaffViewSet(ModelViewSet):
 
    serializer_class = SupportStaffSerializer
 
    def get_queryset(self):
        return SupportStaff.objects.all()


class SalesStaffViewSet(ModelViewSet):
 
    serializer_class = SalesStaffSerializer
 
    def get_queryset(self):
        return SalesStaff.objects.all()
 

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