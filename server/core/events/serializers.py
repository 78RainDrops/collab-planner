from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    participants = serializers.SlugRelatedField(
        many=True,
        slug_field="username",
        queryset=get_user_model().objects.all(),
        required=False,
    )

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_by",
            "created_at",
            "updated_at",
        ]
