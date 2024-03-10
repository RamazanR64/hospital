from rest_framework import viewsets

from .permissions import RoleBasedPermissionMixin, HasPermissionByAuthenticatedUserRole


class HospitalGenericViewSet(
    RoleBasedPermissionMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [HasPermissionByAuthenticatedUserRole]

    # pagination_class = [CustomPagination, ]
