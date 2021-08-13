from rest_framework import serializers
from .models import User

class UserCreationRequestSerializer(serializers.ModelSerializer):

    def create_user(self):
        return User(**self.initial_data)

    class Meta:
        model = User
        fields = ('displayName', 'email', 'password', 'image')


class UserSearchRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'displayName', 'email', 'image')