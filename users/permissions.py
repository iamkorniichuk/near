from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsEmailVerified(BasePermission):
    message = {"email": "Current email is not verified."}

    def has_permission(self, request, view):
        return request.user.is_email_verified


class IsEmailVerifiedOrReadOnly(IsEmailVerified):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or request.method in SAFE_METHODS
