# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.db import models
# from django.utils import timezone
# from django.core.validators import RegexValidator


# class User(AbstractBaseUser, PermissionsMixin):
#     name = models.CharField(max_length=150)

#     email = models.EmailField(
#         unique=True,
#         db_index=True
#     )

#     phone = models.CharField(
#         max_length=20,
#         blank=True,
#         null=True,
#         validators=[
#             RegexValidator(
#                 regex=r"^\+?[0-9\s\-()]{7,20}$",
#                 message="Enter a valid phone number."
#             )
#         ]
#     )

#     is_active = models.BooleanField(default=True)

#     is_staff = models.BooleanField(default=False)

#     created_at = models.DateTimeField(default=timezone.now)

#     USERNAME_FIELD = "email"

#     REQUIRED_FIELDS = ["name"]

#     def __str__(self):
#         return self.email

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(max_length=150)

    email = models.EmailField(
        unique=True,
        db_index=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\+?[0-9\s\-()]{7,20}$",
                message="Enter a valid phone number."
            )
        ]
    )

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email