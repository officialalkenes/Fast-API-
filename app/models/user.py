import uuid
from datetime import datetime as dt

from pydantic import BaseModel

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


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


user_pydantic = pydantic_model_creator(User, name="Users", exclude=("is_verified",))
user_pydanticIn = pydantic_model_creator(User, name="userIn", exclude_readonly=True)
user_pydanticOut = pydantic_model_creator(User, name="UserOut", exclude=("password",))


userprofile_pydantic = pydantic_model_creator(
    UserProfile, name="Profile", exclude=("user",)
)
userprofile_pydanticIn = pydantic_model_creator(
    UserProfile, name="ProfileIn", exclude_readonly=True
)
userprofile_pydanticOut = pydantic_model_creator(
    UserProfile, name="ProfileOut", exclude=("password",)
)
