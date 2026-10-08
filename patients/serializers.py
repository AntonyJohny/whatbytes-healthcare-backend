from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient

        fields = [
            "id",
            "name",
            "email",
            "phone",
            "date_of_birth",
            "address",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


    def validate_name(self, value):

        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Patient name cannot be empty."
            )

        return value