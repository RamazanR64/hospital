from django.contrib.auth.models import Permission
from rest_framework import permissions
from rest_framework.views import APIView

class DoctorAccessPermission(permissions.BasePermission):
    """
    Permission class to check if the user has 'api.view_doctor' permission.
    """
    def has_permission(self, request, view):
        return 'api.view_doctor' in self.get_user_permissions(request.user)

    @staticmethod
    def get_user_permissions(user):
        """
        Returns a set of permission codenames for the given user.
        """
        if user.is_superuser:
            return set(Permission.objects.values_list('codename', flat=True))

        return set(user.user_permissions.values_list('codename', flat=True)) | set(
            Permission.objects.filter(group__user=user).values_list('codename', flat=True))

class RoleBasedPermissionMixin:
    """
    Mixin class to apply role-based permissions to views.
    """
    action_permissions: list[str] = None

    def get_action_permissions(self):
        """
        Get role-based permissions for the current action.
        """
        pass  # Implement in subclasses

    def get_permissions(self):
        """
        Override the default permissions with role-based permissions.
        """
        self.get_action_permissions()
        assert isinstance(self.action_permissions, list), (
            'Expected a `List` type of self.action_permissions '
            'but received a `%s`'
            % type(self.action_permissions)
        )
        return [DoctorAccessPermission()] + super().get_permissions()

class HasPermissionByAuthenticatedUserRole(permissions.BasePermission):
    """
    Permission class to check if the authenticated user has any of the required permissions.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if
