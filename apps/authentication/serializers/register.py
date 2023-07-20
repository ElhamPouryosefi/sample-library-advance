from rest_framework import serializers

from apps.authentication.models.custom_user import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = "__all__"


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    is_author = serializers.BooleanField()





"""
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
"""


def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    print(password)
    instance.set_password(password)
    instance.is_active = True
    instance.save()
    return instance