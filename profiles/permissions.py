from rest_framework.permissions import BasePermission, SAFE_METHODS


class HasProfile(BasePermission):
    message = {"profile": "Current user has no created profile."}

    def has_permission(self, request, view):
        return hasattr(request.user, "profile")


class HasProfileOrReadOnly(HasProfile):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or super().has_permission(request, view)


class IsOwner(BasePermission):
    def __init__(self, field_name="profile"):
        self.message = {field_name: "You need to be owner of this object."}
        self.field_name = field_name

    def has_object_permission(self, request, view, obj):
        obj_profile = obj
        for field in self.field_name.split("."):
            obj_profile = getattr(obj_profile, field)

        return obj_profile == request.user.profile


class IsOwnerOrReadOnly(IsOwner):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or super().has_object_permission(
            request, view, obj
        )
