
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={"input_type": "password"},
    )

    class Meta:
        model = User
        fields = ["id", "name", "email", "password"]

    def create(self, validated_data):
        email = validated_data["email"].lower()
        username = email

        return User.objects.create_user(
            username=username,
            email=email,
            name=validated_data["name"],
            password=validated_data["password"],
        )
