from rest_framework import serializers

from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor

        fields = [
            "id",
            "name",
            "specialization",
            "email",
            "phone",
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
                "Doctor name cannot be empty."
            )

        return value


    def validate_specialization(self, value):

        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Specialization cannot be empty."
            )

        return value