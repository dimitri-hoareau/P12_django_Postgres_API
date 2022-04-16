from cgitb import reset
from multiprocessing import Event
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import SalesStaff, GestionStaff, SupportStaff, Event


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
        return True

    def has_object_permission(self, request, view, obj):

        user_status = FindUserStatus.find_user_status(request.user)
        print(user_status)
        # faire avec exist qui renvoit un bool
        # salesStaff = SalesStaff.objects.filter(client=obj.id)
        # for staff in SalesStaff:
        #     if request.user == staff.user:
        #         is_sales_staff = True

        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if  request.method in SAFE_METHODS :
            return True
        # return obj.author == request.user
        return True

class ContractIsAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):

        authorized_user = ['gestion_staff', 'sales_staff']

        user_status = FindUserStatus.find_user_status(request.user)
        print(user_status)
        print(request.method)
        print(SAFE_METHODS)

        if user_status in authorized_user:
            print("ok")

        if  request.method in SAFE_METHODS :
            return True
        # return obj.author == request.user
        return True


class EventIsAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        user_status = FindUserStatus.find_user_status(request.user)
        authorized_users_to_post = user_status in ['gestion_staff','sales_staff']

        if request.method == 'POST':
            return authorized_users_to_post
        
        return True

    def has_object_permission(self, request, view, obj):
        user_status = FindUserStatus.find_user_status(request.user)

        if  request.method in SAFE_METHODS :
            return True
            
        elif request.method == 'PUT':
            event_support_staff = 'first_turn'
            try:
                event_support_staff = obj.support_staff
            except:
                pass
            if event_support_staff == 'first_turn':
                return True
            return str(event_support_staff) == str(request.user)

        else:
            return user_status == 'gestion_staff'

        

