from rest_framework.permissions import IsAdminUser, SAFE_METHODS, BasePermission
from rest_framework import permissions
from django.contrib.auth.models import Group



def _is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


def _has_group_permission(user, required_groups):
    return any([_is_in_group(user, group_name) for group_name in required_groups])
class IsManager(BasePermission):
    def has_permission(self, request, view=None):
        if request.user.is_active and request.user.is_staff:
            return True
        return False


class IsSales(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj.author_user_id == request.user

class IsSupport(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author_user_id == request.user

class CheckPermission(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH", "DELETE")
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author_user_id == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False

