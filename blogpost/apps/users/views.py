from __future__ import annotations

from apps.users.models import User
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from utils import create_id

from .authentication import generate_token
from .authentication import get_user
from .authentication import hash_password
from .authentication import is_authorized
from .authentication import validate_password
from .serializers import UserCreationRequestSerializer
from .serializers import UserSearchRequestSerializer


class UserView(APIView):

    def post(self, request):

        user_data = JSONParser().parse(request)
        serializer = UserCreationRequestSerializer(data=user_data)
        user = serializer.create_user()

        if not user.has_valid_display_name():
            return JsonResponse({'message': user.notification}, status=status.HTTP_400_BAD_REQUEST)

        if not user.has_valid_email():
            return JsonResponse({'message': user.notification}, status=status.HTTP_400_BAD_REQUEST)

        if not user.has_valid_password():
            return JsonResponse({'message': user.notification}, status=status.HTTP_400_BAD_REQUEST)

        if user.has_existing_email():
            return JsonResponse({'message': user.notification}, status=status.HTTP_409_CONFLICT)

        user.id = create_id('usr')
        user.password = hash_password(user.password)
        user.save()

        return JsonResponse({'token': generate_token(user)}, status=status.HTTP_201_CREATED)

    @is_authorized()
    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSearchRequestSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)


class UserDetailsView(APIView):

    @is_authorized()
    def get(self, request, id):
        user = self.get_user_from_id(id)

        if user is None:
            return JsonResponse({'message': 'Usuário não existe'}, status=status.HTTP_404_NOT_FOUND)

        users_serializer = UserSearchRequestSerializer(user)
        return JsonResponse(users_serializer.data, safe=False)

    def get_user_from_id(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class CurrentUserView(APIView):

    @is_authorized()
    def get(self, request):

        user = get_user(request)
        if user is None:
            return JsonResponse({'message': 'Usuário não existe'}, status=status.HTTP_404_NOT_FOUND)

        users_serializer = UserSearchRequestSerializer(user)
        return JsonResponse(users_serializer.data, safe=False)

    @is_authorized()
    def delete(self, request):
        user = get_user(request)
        user.delete()

        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):

    def post(self, request):

        login_data = JSONParser().parse(request)

        if 'email' not in login_data:
            return JsonResponse({'message': '"email" is required'}, status=status.HTTP_400_BAD_REQUEST)

        if not login_data['email']:
            return JsonResponse({'message': '"email" is not allowed to be empty'}, status=status.HTTP_400_BAD_REQUEST)

        if 'password' not in login_data:
            return JsonResponse({'message': '"password" is required'}, status=status.HTTP_400_BAD_REQUEST)

        if not login_data['password']:
            return JsonResponse(
                {'message': '"password" is not allowed to be empty'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.filter(email=login_data['email'])

        if not user or not validate_password(login_data['password'], user.first().password):
            return JsonResponse({'message': 'Campos inválidos'}, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({'token': generate_token(user.first())}, status=status.HTTP_200_OK)
