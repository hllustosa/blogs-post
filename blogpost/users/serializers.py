from rest_framework import serializers
from .models import User

class UserCreationRequestRequestSerializer(serializers.ModelSerializer):

    def create_user(self):
        return User(**self.initial_data)

    class Meta:
        model = User
        fields = ('displayName', 'email', 'password', 'image')