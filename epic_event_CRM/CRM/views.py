from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from CRM.permissions import ClientIsAuthorOrReadOnly, ContractIsAuthorOrReadOnly, EventIsAuthorOrReadOnly
 
from CRM.models import Client, Contract, Event, SalesStaff, GestionStaff, SupportStaff
from CRM.serializers import ClientSerializer, ContractSerializer, EventSerializer, SalesStaffSerializer, GestionStaffSerializer, SupportStaffSerializer



class GestionStaffViewSet (ModelViewSet):
 
    serializer_class = GestionStaffSerializer
    # permission_classes = [IsAuthenticated]
 
    def get_queryset(self):
        return GestionStaff.objects.all()

class SupportStaffViewSet(ModelViewSet):
 
    serializer_class = SupportStaffSerializer
    # permission_classes = [IsAuthenticated]
 
    def get_queryset(self):
        return SupportStaff.objects.all()


class SalesStaffViewSet(ModelViewSet):
 
    serializer_class = SalesStaffSerializer
    # permission_classes = [IsAuthenticated]
 
    def get_queryset(self):
        return SalesStaff.objects.all()
 

class ClientViewSet(ModelViewSet):
 
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated,ClientIsAuthorOrReadOnly]
 
    def get_queryset(self):
        print(self.request.user)

        obj = Client.objects.all()
        client_name = self.request.GET.get('client_name')
        client_email = self.request.GET.get('client_email')
        if client_name is not None:
            obj = obj.filter(last_name=client_name)
        if client_email is not None:
            obj = obj.filter(email=client_email)
        self.check_object_permissions(self.request, obj)
        return obj

class ContractViewSet(ModelViewSet):
 
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated,ContractIsAuthorOrReadOnly]
 
    def get_queryset(self):
        obj = Contract.objects.all()
        client_name = self.request.GET.get('client_name')
        client_email = self.request.GET.get('client_email')
        contract_date = self.request.GET.get('contract_date')
        contract_amount = self.request.GET.get('contract_amount')

        if client_name is not None:
            client = Client.objects.filter(last_name=client_name)
            obj = obj.filter(client__in=client)
        if client_email is not None:
            client = Client.objects.filter(email=client_email)
            obj = obj.filter(client__in=client)
        if contract_date is not None:
            obj = obj.filter(date_created=contract_date)
        if contract_amount is not None:
            obj = obj.filter(amount=contract_amount)

        self.check_object_permissions(self.request, obj)
        return obj

class EventViewSet(ModelViewSet):
 
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, EventIsAuthorOrReadOnly]
 
    def get_queryset(self):
        obj = Event.objects.all()
        client_name = self.request.GET.get('client_name')
        client_email = self.request.GET.get('client_email')
        event_date = self.request.GET.get('event_date')

        if client_name is not None:
            client = Client.objects.filter(last_name=client_name)
            obj = obj.filter(client__in=client)
        if client_email is not None:
            client = Client.objects.filter(email=client_email)
            obj = obj.filter(client__in=client)
        if event_date is not None:
            obj = obj.filter(event_date=event_date)


        self.check_object_permissions(self.request, obj)
        return obj