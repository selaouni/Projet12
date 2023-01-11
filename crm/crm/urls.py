"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from authentication.views import RegisterView, UserByProjectView
from rest_framework_simplejwt.views import TokenObtainPairView

from crmapplication.views import EventViewset, ContractViewset
from crmapplication.views import ClientViewset


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('crmapplication.urls')),

 ]














# from crmapplication.views SalesViewset, SupportViewset


#
#
# router = routers.SimpleRouter()
# router.register('client', ClientViewset, basename='client')
# router.register('event', EventViewset, basename='event')
# router.register('contract', ContractViewset, basename='contract')
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/signup/', RegisterView.as_view()),
#     path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api-auth/', include('rest_framework.urls')),
#     path('api/', include(router.urls)),
#     ]

