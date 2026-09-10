from django.contrib.auth.models import User
from django.db import models


class Role(models.TextChoices):
    CUSTOMER = "customer", "Customer"
    SELLER = "seller", "Seller"
    SUPPORT = "support", "Support"
    ADMIN = "admin", "Admin"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=16, unique=True)
    role = models.CharField(max_length=16, choices=Role.choices, default=Role.CUSTOMER)


class OTPChallenge(models.Model):
    phone_number = models.CharField(max_length=16, db_index=True)
    code_digest = models.CharField(max_length=64)
    expires_at = models.DateTimeField()
    attempts = models.PositiveSmallIntegerField(default=0)
    consumed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
