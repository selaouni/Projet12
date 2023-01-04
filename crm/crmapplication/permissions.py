from rest_framework.permissions import IsAdminUser, SAFE_METHODS, BasePermission
from rest_framework import permissions


class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        # is_admin = super(
        #     IsAdminUserOrReadOnly,
        #     self).has_permission(request, view)
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


#management role
class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj.author_user_id == request.user

class IsSales:
    message = 'operation not allowed.'

    def has_permission(self, request, view):
        pass


class IsSupport:
    message = 'operation  not allowed.'

    def has_permission(self, request, view):
        pass


