"""epic_event_CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from CRM.views import ClientViewSet, ContractViewSet, EventViewSet, SalesStaffViewSet, GestionStaffViewSet, SupportStaffViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.SimpleRouter()

router.register('client', ClientViewSet, basename='client')
router.register('contract', ContractViewSet, basename='contract')
router.register('event', EventViewSet, basename='event')
# router.register('sales_staff', SalesStaffViewSet, basename='sales_staff')
# router.register('gestion_staff', GestionStaffViewSet, basename='gestion_staff')
# router.register('support_staff', SupportStaffViewSet, basename='support_staff')
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))  
]
