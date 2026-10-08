from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer


class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer

    def get_queryset(self):
        return (
            PatientDoctorMapping.objects.filter(
                patient__created_by=self.request.user
            )
            .select_related("patient", "doctor")
        )


class MappingDetailView(APIView):
    """
    GET:
        /api/mappings/<patient_id>/
        Returns all doctors assigned to the patient.

    DELETE:
        /api/mappings/<mapping_id>/
        Deletes the specified patient-doctor mapping.

    The assignment uses the same URL pattern for these two operations,
    so the HTTP method determines the operation.
    """

    def get(self, request, pk):
        mappings = (
            PatientDoctorMapping.objects.filter(
                patient_id=pk,
                patient__created_by=request.user,
            )
            .select_related("patient", "doctor")
        )

        serializer = PatientDoctorMappingSerializer(
            mappings,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        mapping = get_object_or_404(
            PatientDoctorMapping,
            pk=pk,
            patient__created_by=request.user,
        )

        mapping.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)