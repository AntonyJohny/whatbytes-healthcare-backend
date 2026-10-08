from django.urls import path

from .views import (
    MappingListCreateView,
    PatientMappingListView,
    MappingDeleteView,
)

urlpatterns = [
    # Create mapping / list mappings
    path(
        "",
        MappingListCreateView.as_view(),
        name="mapping-list-create",
    ),

    # Get all doctors assigned to a specific patient
    path(
        "patient/<int:patient_id>/",
        PatientMappingListView.as_view(),
        name="patient-mappings",
    ),

    # Delete a specific mapping
    path(
        "<int:pk>/",
        MappingDeleteView.as_view(),
        name="mapping-delete",
    ),
]