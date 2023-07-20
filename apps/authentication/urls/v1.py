from django.urls import path
from rest_framework.authtoken import views
from apps.authentication.views.v1 import LogoutAPIView, Register, ChangePassword, Register1

urlpatterns = [
    path('login/', views.obtain_auth_token, name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('createaccount/', Register.as_view(), name='register'),
    path('createaccount1/', Register1.as_view(), name='register1'),
    path('password/', ChangePassword.as_view(), name='password'),
]
