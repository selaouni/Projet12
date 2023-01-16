
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterView, UserByProjectView


urlpatterns = [

    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/signup/', RegisterView.as_view()),
    path('api-auth/', include('rest_framework.urls')),

    ]
