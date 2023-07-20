from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission

from common.messages import PermissionMsg
from core.library_modules.utilities import AuthPermission


class UserPermission(BasePermission):
    message = PermissionMsg.AUTHENTICATION_FAILED

    def has_permission(self, request, view):
        return bool(request.user)


class CheckPermission(BasePermission):
    message = PermissionMsg.NO_ACCESS_TO_VIEW

    def has_permission(self, request, view):
        if not hasattr(view, 'permission_name'):
            return True
        if request.method not in view.permission_name:
            return True
        if not hasattr(request, 'user'):
            return False
        if type(request.user) == AnonymousUser:
            return False
        if request.user.is_superuser or hasattr(request.user, 'is_admin'):
            return True
        user = AuthPermission(request.user)
        if hasattr(view, 'second_permission_name'):
            status = user.has_perm(view.permission_name[request.method]) or user.has_perm(
                view.second_permission_name)
            if not status:
                return False
        else:
            status = user.has_perm(view.permission_name[request.method])
            if not status:
                return False
        return True
