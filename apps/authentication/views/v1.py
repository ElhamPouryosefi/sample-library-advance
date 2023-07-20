from rest_framework import permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.models.custom_user import CustomUser
from apps.authentication.serializers.change_password import ChangePasswordSerializer
from apps.authentication.serializers.register import RegisterSerializer, CustomUserSerializer


class Register1(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]


class Register(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user_serializer = CustomUserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response({'message': 'welcome'})


class LogoutAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        request.user.auth_token.delete()
        return Response(data={'message': f"Bye {request.user.username}!"})


class ChangePassword(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
