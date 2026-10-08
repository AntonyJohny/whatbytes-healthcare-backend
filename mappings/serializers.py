from rest_framework import serializers

from .models import PatientDoctorMapping


class PatientDoctorMappingSerializer(
    serializers.ModelSerializer
):

    patient_name = serializers.CharField(
        source="patient.name",
        read_only=True
    )

    doctor_name = serializers.CharField(
        source="doctor.name",
        read_only=True
    )

    doctor_specialization = serializers.CharField(
        source="doctor.specialization",
        read_only=True
    )

    class Meta:

        model = PatientDoctorMapping

        fields = [
            "id",
            "patient",
            "patient_name",
            "doctor",
            "doctor_name",
            "doctor_specialization",
            "assigned_at",
        ]

        read_only_fields = [
            "id",
            "patient_name",
            "doctor_name",
            "doctor_specialization",
            "assigned_at",
        ]

    def validate(self, attrs):

        patient = attrs["patient"]
        doctor = attrs["doctor"]

        request = self.context["request"]

        if patient.created_by != request.user:
            raise serializers.ValidationError(
                {
                    "patient":
                    "You can only assign doctors to your own patients."
                }
            )

        if PatientDoctorMapping.objects.filter(
            patient=patient,
            doctor=doctor
        ).exists():

            raise serializers.ValidationError(
                "This doctor is already assigned to this patient."
            )

        return attrs