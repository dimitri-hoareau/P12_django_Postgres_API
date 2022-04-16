from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from CRM.permissions import ClientIsAuthorOrReadOnly, ContractIsAuthorOrReadOnly, EventIsAuthorOrReadOnly
 
from CRM.models import Client, Contract, Event, SalesStaff, GestionStaff, SupportStaff
from CRM.serializers import ClientSerializer, ContractSerializer, EventSerializer, SalesStaffSerializer, GestionStaffSerializer, SupportStaffSerializer


def find_user_status(request_user):

    def check_user_status(model, request_user, user_status):
        
        queryset = model.objects.all()

        for user in queryset:
            if request_user == user:
                return "sales_staff"
        return None

    sales_staff = check_user_status(SalesStaff, request_user, "sales_staff")
    if sales_staff is None:
        support_staff = check_user_status(SupportStaff, request_user, "support_staff")
        if support_staff is None:
            return "gestion_staff"
        return support_staff
    return sales_staff



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
        self.check_object_permissions(self.request, obj)
        return obj

class ContractViewSet(ModelViewSet):
 
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated,ContractIsAuthorOrReadOnly]
 

    def get_queryset(self):
        obj = Contract.objects.all()
        self.check_object_permissions(self.request, obj)
        return obj

class EventViewSet(ModelViewSet):
 
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, EventIsAuthorOrReadOnly]
 
    def get_queryset(self):
        obj = Event.objects.all()
        self.check_object_permissions(self.request, obj)
        return obj