from rest_framework import serializers

from apps.authentication.models.custom_user import CustomUser


class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser
    old_password = serializers.CharField()
    new_password = serializers.CharField()
