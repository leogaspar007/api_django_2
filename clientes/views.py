from rest_framework import viewsets
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', 'id']
    search_fields = ['nome', 'cpf', 'rg', 'email', 'celular', 'id']
    filterset_fields = ['ativo']
