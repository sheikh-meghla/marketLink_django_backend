from django.http import Http404
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    SignUpView,
    SignInView,
    SignOutView,
    ChangePasswordView,
    UpdateProfileView,
    MyProfileView,
    SwitchRoleView,
)

urlpatterns = [

    # Authentications

    path("signup/", SignUpView.as_view(), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path("signout/", SignOutView.as_view(), name="signout"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token_refresh"),


    # password
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    
    # profile
    path('update-profile/', UpdateProfileView.as_view(), name='profile-update'),
    path('my-profile/', MyProfileView.as_view(), name='profile-get'),


    # switch role

    path("switch-role/", SwitchRoleView.as_view(), name="switch-role"),
]
