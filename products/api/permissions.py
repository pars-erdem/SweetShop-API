from rest_framework import permissions
class IsSuperUserOrReadWrite(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method in ['PUT', 'PATCH']:
            return request.user and request.user.is_authenticated
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method in ['PUT', 'PATCH']:
            return request.user and request.user.is_authenticated
        return False
class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin