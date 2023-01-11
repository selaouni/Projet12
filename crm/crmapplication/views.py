from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly, IsAdminUser,  IsManager, IsSales, IsSupport
from django.db.models import Q


from .models import Client, Contract, Event, Event_status, Sales,Support
from .serializers import ClientSerializer
from .serializers import ContractSerializer, EventSerializer
from .serializers import SalesSerializer, SupportSerializer


class ClientViewset(ModelViewSet):
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    permission_classes = [(IsAdminUser | IsAuthenticated) & (IsSales | IsSupport)]


    serializer_class = ClientSerializer

    def get_queryset(self, *args, **kwargs):
        # Nous récupérons tous les produits dans une variable nommée queryset
        # user = self.request.user
        queryset = Client.objects.all()

        # Vérifions la présence du paramètre ‘project_id’ dans l’url et si oui alors appliquons notre filtre
        client_id = self.request.GET.get('client_id')

        if client_id is not None:
            queryset = queryset.filter(client_id=client_id)

        return queryset

    def put_queryset(self, request, pk):
        queryset = self.get_object(pk)
        serializer = ClientSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_queryset(self):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post_queryset(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EventViewset(ModelViewSet):
    permission_classes = [(IsAdminUser | IsAuthenticated) & (IsSales | IsSupport)]
    serializer_class = EventSerializer

    def get_queryset(self, *args, **kwargs):

        # user = self.request.user
        queryset = Event.objects.all()
        event_id = self.request.GET.get('event_id')
        if event_id is not None:
            queryset = queryset.filter(event_id=event_id)


        return queryset

    def put_queryset(self, request, pk):
        queryset = self.get_object(pk)
        serializer = EventSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_queryset(self):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post_queryset(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ContractViewset(ModelViewSet):
    permission_classes = [(IsAdminUser | IsAuthenticated) & (IsSales | IsSupport)]
    # permission_classes = [And(Or(IsAdminUser, IsAuthenticated), IsOwnerOrReadOnly)]
    serializer_class = ContractSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Contract.objects.all()
        # user = self.request.user
        contract_id = self.request.GET.get('contract_id')

        if contract_id is not None :
            queryset = queryset.filter(contract_id=contract_id)

        return queryset

    def put_queryset(self, request, pk):
        queryset = self.get_object(pk)
        serializer = ContractSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_queryset(self, format=None):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post_queryset(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



























#
# class SalesViewset(ModelViewSet):
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
#     queryset = Contributor.objects.all().select_related('project_id').prefetch_related('user_id')
#     serializer_class = ContributorSerializer
#
#     def get_queryset(self, *args, **kwargs):
#         project_id = self.kwargs.get("project_pk")
#         try:
#             project = Project.objects.get(id=project_id)
#         except Project.DoesNotExist:
#             print('A project with this id does not exist')
#         return self.queryset.filter(project_id=project_id)
#
#
# class SupportViewset(ModelViewSet):
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
#     queryset = Contributor.objects.all().select_related('project_id').prefetch_related('user_id')
#     serializer_class = ContributorSerializer
#
#     def get_queryset(self, *args, **kwargs):
#         project_id = self.kwargs.get("project_pk")
#         try:
#             project = Project.objects.get(id=project_id)
#         except Project.DoesNotExist:
#             print('A project with this id does not exist')
#         return self.queryset.filter(project_id=project_id)