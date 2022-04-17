from cgitb import reset
from multiprocessing import Event
from multiprocessing.connection import Client
from tkinter.messagebox import QUESTION
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import SalesStaff, GestionStaff, SupportStaff, Event, Client, Contract


class FindUserStatus(): 
    def find_user_status(request_user):

        def check_user_status(model, request_user, user_status):
            
            queryset = model.objects.all()

            for user in queryset:
                if str(request_user) == str(user):
                    return user_status
            return None

        sales_staff = check_user_status(SalesStaff, request_user, "sales_staff")

        if sales_staff is None:
            support_staff = check_user_status(SupportStaff, request_user, "support_staff")
            if support_staff is None:
                return "gestion_staff"
            return support_staff
        return sales_staff


class ClientIsAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        user_status = FindUserStatus.find_user_status(request.user)
        authorized_users_to_post = user_status in ['gestion_staff','sales_staff']
        if request.method == 'POST':
            return authorized_users_to_post
        
        return True

    def has_object_permission(self, request, view, obj):

        user_status = FindUserStatus.find_user_status(request.user)

        if user_status == 'gestion_staff':
            return True

        elif request.method in SAFE_METHODS :
            return True

        elif request.method == 'PUT':
            event_sales_staff = 'first_turn'
            try:
                event_sales_staff = obj.sales_staff
            except:
                pass
            if event_sales_staff == 'first_turn':
                return True
            return str(event_sales_staff) == str(request.user)

        else:
            return user_status == 'gestion_staff'

class ContractIsAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        user_status = FindUserStatus.find_user_status(request.user)
        authorized_users_to_post = user_status in ['gestion_staff','sales_staff']
        if request.method == 'POST':
            return authorized_users_to_post
        
        return True

    def has_object_permission(self, request, view, obj):
        user_status = FindUserStatus.find_user_status(request.user)
        if user_status == 'gestion_staff':
            return True

        elif  request.method in SAFE_METHODS :
            return True
            
        elif request.method == 'PUT' and user_status == 'sales_staff':

            client_event_sales_staff = 'first_turn'
            try:
                client_event_sales_staff = obj.client
            except:
                pass
            if client_event_sales_staff == 'first_turn':
                return True
     
            request_user_clients = SalesStaff.objects.filter(user=request.user)
            sales_staff_client = Client.objects.filter(sales_staff=request_user_clients[0])
            is_contract_attributed_to_user_client = sales_staff_client.filter(id=client_event_sales_staff.id).exists()

            return is_contract_attributed_to_user_client

        else:
            return user_status == 'gestion_staff'



class EventIsAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        user_status = FindUserStatus.find_user_status(request.user)
        authorized_users_to_post = user_status in ['gestion_staff','sales_staff']

        if request.method == 'POST':
            return authorized_users_to_post
        
        return True

    def has_object_permission(self, request, view, obj):
        user_status = FindUserStatus.find_user_status(request.user)

        if user_status == 'gestion_staff':
            return True

        elif  request.method in SAFE_METHODS :
            return True
            
        elif request.method == 'PUT' and user_status == 'support_staff':

            event_support_staff = 'first_turn'
            try:
                event_support_staff = obj.support_staff
            except:
                pass
            if event_support_staff == 'first_turn':
                return True
            return str(event_support_staff) == str(request.user)

        elif request.method == 'PUT' and user_status == 'sales_staff':

            client_event_sales_staff = 'first_turn'
            try:
                client_event_sales_staff = obj.client
            except:
                pass
            if client_event_sales_staff == 'first_turn':
                return True
     
            request_user_clients = SalesStaff.objects.filter(user=request.user)
            sales_staff_client = Client.objects.filter(sales_staff=request_user_clients[0])
            is_event_attributed_to_user_client = sales_staff_client.filter(id=client_event_sales_staff.id).exists()

            return is_event_attributed_to_user_client

        else:
            return user_status == 'gestion_staff'

        

