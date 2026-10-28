
from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.views import RegisterView
from doctors.views import MappingListCreateView, MappingDetailView


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Authentication APIs
    path(
        "api/auth/register/",
        RegisterView.as_view(),
        name="register",
    ),
    path(
        "api/auth/login/",
        TokenObtainPairView.as_view(
            permission_classes=[AllowAny]
        ),
        name="login",
    ),
    path(
        "api/auth/token/refresh/",
        TokenRefreshView.as_view(
            permission_classes=[AllowAny]
        ),
        name="token_refresh",
    ),

    # Patient management APIs
    path(
        "api/patients/",
        include("patients.urls"),
    ),

    # Doctor management APIs
    path(
        "api/doctors/",
        include("doctors.urls"),
    ),

    # Patient-doctor mapping APIs
    path(
        "api/mappings/",
        MappingListCreateView.as_view(),
        name="mapping-list-create",
    ),
    path(
        "api/mappings/<int:pk>/",
        MappingDetailView.as_view(),
        name="mapping-detail",
    ),
]
