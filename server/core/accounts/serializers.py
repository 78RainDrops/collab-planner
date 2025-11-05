from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "email", "role")

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            role=validated_data.get("role", "member"),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
