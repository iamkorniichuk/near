from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsEmailVerified(IsAuthenticated):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            self.message = {"email": "Current email is not verified."}
            return request.user.is_email_verified
        return False


class IsEmailVerifiedOrReadOnly(IsEmailVerified):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or request.method in SAFE_METHODS
