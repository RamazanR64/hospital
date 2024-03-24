from api.mixins import HospitalGenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters, permissions

from api.models import Patient
from api.serializers import (
    PatientListSerializer,
    PatientDetailedSerializer,
    PatientCreateOrUpdateSerializer
)

class PatientViewSet(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'
    queryset = Patient.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['gender']
    search_fields = ['first_name', 'last_name']

    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        if self.action in ('retrieve', 'update', 'create'):
            return PatientCreateOrUpdateSerializer
        if self.action == 'destroy':
            return PatientDetailedSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [permissions.IsAuthenticated, 'view_patient']
        elif self.action == 'create':
            self.permission_classes = [permissions.IsAuthenticated, 'add_patient']
        elif self.action == 'update':
            self.permission_classes = [permissions.IsAuthenticated, 'change_patient']
        elif self.action == 'destroy':
            self.permission_classes = [permissions.IsAuthenticated, 'delete_patient']
        return super().get_permissions()
