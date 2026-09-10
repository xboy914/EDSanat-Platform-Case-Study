from rest_framework.permissions import BasePermission

from .models import Role


class HasPlatformRole(BasePermission):
    def has_permission(self, request, view) -> bool:
        if not request.user or not request.user.is_authenticated:
            return False
        allowed = getattr(view, "allowed_roles", {Role.CUSTOMER})
        try:
            return request.user.profile.role in allowed
        except AttributeError:
            return False
