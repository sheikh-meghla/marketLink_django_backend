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
    ProfileGet,
)

urlpatterns = [

    path("signup/", SignUpView.as_view(), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path("signout/", SignOutView.as_view(), name="signout"),

    # password
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    
    # profile
    path('profile-update/', UpdateProfileView.as_view(), name='profile-update'),
    path('profile-get/', ProfileGet.as_view(), name='profile-get'),

    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
