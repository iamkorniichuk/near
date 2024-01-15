from rest_framework.permissions import BasePermission


class HasUnverifiedEmail(BasePermission):
    message = {"email": "Email has been already verified."}

    def has_permission(self, request, view):
        return not request.user.is_email_verified
