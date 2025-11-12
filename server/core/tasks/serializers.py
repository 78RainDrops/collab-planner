from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Task


class TaskSerializers(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(
        slug_field="username",
        queryset=get_user_model().objects.all(),
    )

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = [
            "id",
            "event",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        event = attrs.get("event") or getattr(self.instance, "event", None)
        assigned_to = attrs.get("assigned_to")

        if event and assigned_to and assigned_to not in event.participants.all():
            raise serializers.ValidationError(
                "User must be a participant of the event."
            )
        return attrs
