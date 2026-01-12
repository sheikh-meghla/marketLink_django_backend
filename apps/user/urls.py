from django.http import Http404
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    SignUpAPIView,
    SignInAPIView,
    SignOutAPIView,
    ChangePasswordAPIView,
    UpdateProfileAPIView,
    MyProfileAPIView,
    SwitchRoleAPIView,
)

urlpatterns = [

    # Authentications

    path("signup/", SignUpAPIView.as_view(), name="signup"),
    path("signin/", SignInAPIView.as_view(), name="signin"),
    path("signout/", SignOutAPIView.as_view(), name="signout"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token_refresh"),


    # password
    path('change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
    
    # profile
    path('update-profile/', UpdateProfileAPIView.as_view(), name='profile-update'),
    path('my-profile/', MyProfileAPIView.as_view(), name='profile-get'),


    # switch role

    path("switch-role/", SwitchRoleAPIView.as_view(), name="switch-role"),
]
