import uuid
from datetime import datetime as dt

from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.UUIDField(default=uuid.uuid4, pk=True, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=20)
    is_verified = fields.BooleanField(default=False)
    is_owner = fields.BooleanField(default=False)
    is_admin = fields.BooleanField(default=False)
    created = fields.DatetimeField(default=dt.utcnow)
    updated = fields.DatetimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.email}"


class UserProfile(Model):
    id = fields.UUIDField(default=uuid.uuid4, pk=True, unique=True)
    user = fields.OneToOneField("models.User", on_delete=fields.CASCADE)
    birth_date = fields.DateField(null=True)
    country = fields.CharField(null=False, max_length=20, default="Unspecified")
