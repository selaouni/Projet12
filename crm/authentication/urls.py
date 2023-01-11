
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [

    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-auth/', include('rest_framework.urls')),

    ]