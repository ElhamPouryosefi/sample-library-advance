from rest_framework.permissions import BasePermission
from rest_framework.views import APIView

from .permission_handler import UserPermission, CheckPermission


class UserAPIView(APIView):
    """
    registered user view
    """
    permission_classes = [UserPermission, CheckPermission]
    # permission_classes = (BasePermission,)


class NoAuthAPIView(APIView):
    """
    all users view
    """
    permission_classes = (BasePermission,)
