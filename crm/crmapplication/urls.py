from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from crmapplication.views import EventViewset, ContractViewset
from crmapplication.views import ClientViewset

router = routers.SimpleRouter()
router.register('client', ClientViewset, basename='client')
router.register('event', EventViewset, basename='event')
router.register('contract', ContractViewset, basename='contract')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    ]