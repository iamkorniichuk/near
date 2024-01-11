from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class HasProfile(IsAuthenticated):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            self.message = {"profile": "Current user has no created profile."}
            return hasattr(request.user, "profile")
        return False


class HasProfileOrReadOnly(HasProfile):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or request.method in SAFE_METHODS
