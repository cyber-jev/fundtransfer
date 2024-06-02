# from django.db import models
# from django.contrib.auth.models import AbstractUser


# # Create your models here.
# class User(AbstractUser):
#     phone_number = models.CharField(max_length=15, unique=True)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
#     is_superuser = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)

#     USERNAME_FIELD = "phone_number"
#     REQUIRED_FIELDS = ["username", "email"]

#     def __str__(self):
#         return self.phone_number


from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Add a unique related_name
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",  # Add a unique related_name
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user",
    )

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username", "email"]

    def __str__(self):
        return self.phone_number
