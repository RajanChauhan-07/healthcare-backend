
from django.urls import path

from .views import (
    DoctorListCreateView,
    DoctorDetailView,
    MappingListCreateView,
    MappingDetailView,
)

urlpatterns = [
    # Doctor management APIs
    path(
        "",
        DoctorListCreateView.as_view(),
        name="doctor-list-create",
    ),
    path(
        "<int:pk>/",
        DoctorDetailView.as_view(),
        name="doctor-detail",
    ),

    # Mapping APIs
    path(
        "mappings/",
        MappingListCreateView.as_view(),
        name="mapping-list-create",
    ),
    path(
        "mappings/<int:pk>/",
        MappingDetailView.as_view(),
        name="mapping-detail",
    ),
]
