from rest_framework.permissions import BasePermission, SAFE_METHODS


class HasProfile(BasePermission):
    message = {"profile": "Current user has no created profile."}

    def has_permission(self, request, view):
        return hasattr(request.user, "profile")


class HasProfileOrReadOnly(HasProfile):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or request.method in SAFE_METHODS
