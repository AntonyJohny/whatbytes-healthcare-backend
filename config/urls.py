# from django.contrib import admin
# from django.urls import include, path
# from rest_framework_simplejwt.views import TokenRefreshView

# urlpatterns = [
#     path("admin/", admin.site.urls),

#     # DRF browser login
#     path("api-auth/", include("rest_framework.urls")),

#     # JWT authentication
#     path("api/auth/", include("accounts.urls")),
#     path(
#         "api/auth/token/refresh/",
#         TokenRefreshView.as_view(),
#         name="token-refresh",
#     ),

#     # APIs
#     path("api/patients/", include("patients.urls")),
#     path("api/doctors/", include("doctors.urls")),
#     path("api/mappings/", include("mappings.urls")),
# ]


from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api-auth/",
        include("rest_framework.urls"),
    ),

    path(
        "api/auth/",
        include("accounts.urls"),
    ),

    path(
        "api/auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token-refresh",
    ),

    path(
        "api/patients/",
        include("patients.urls"),
    ),

    path(
        "api/doctors/",
        include("doctors.urls"),
    ),

    path(
        "api/mappings/",
        include("mappings.urls"),
    ),
]