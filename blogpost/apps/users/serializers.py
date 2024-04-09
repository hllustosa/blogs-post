from __future__ import annotations

from apps.users.models import User
from apps.users.password import hash_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import serializers
from utils.id import create_id


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'displayName', 'password', 'email', 'image']
        read_only_fields = ['id']

    def create(self, validated_data):
        validated_data['id'] = create_id('user')
        validated_data['password'] = hash_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.displayName = validated_data.get(
            'displayName', instance.displayName,
        )
        instance.email = validated_data.get('email', instance.email)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

    def validate_displayName(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                'displayName length must be at least 8 characters long',
            )
        return value

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError('email must be a valid email')
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                'password length must be at least 8 characters long',
            )
        return value

    def validate(self, data):
        email = data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User already exists')
        return data

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('password')
        return ret


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False)
