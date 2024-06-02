from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "phone_number", "username", "balance"]
        extra_kwargs = {"balance": {"read_only": True}}
