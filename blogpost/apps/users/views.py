from __future__ import annotations

from apps.users.filters import UserFilter
from apps.users.models import User
from apps.users.password import validate_password
from apps.users.serializers import LoginSerializer
from apps.users.serializers import UserSerializer
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from utils.permission import BlogPostCreateListUserPermission
from utils.permission import BlogPostPermission
from utils.token import generate_token
from utils.token import get_user_id


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [BlogPostCreateListUserPermission]
    filterset_class = UserFilter


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [BlogPostPermission]
    filterset_class = UserFilter


class CurrentUserView(APIView):

    def get(self, request):
        current_user_id = get_user_id(request)
        user = get_object_or_404(User, pk=current_user_id)
        users_serializer = UserSerializer(user)
        return JsonResponse(users_serializer.data, safe=False)


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        login_data = serializer.data
        user = User.objects.filter(email=login_data['email']).first()

        if not user or not validate_password(login_data['password'], user.password):
            return JsonResponse({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return JsonResponse({'token': generate_token(user)}, status=status.HTTP_200_OK)
