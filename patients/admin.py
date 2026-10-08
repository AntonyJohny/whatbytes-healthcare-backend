from django.contrib import admin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "name",
        "email",
        "phone",
        "created_by",
        "created_at",
    ]

    search_fields = [
        "name",
        "email",
        "phone",
    ]