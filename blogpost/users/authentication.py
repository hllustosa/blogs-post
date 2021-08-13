import datetime
import jwt
from argon2 import PasswordHasher
from .models import User
from blogpost.settings import SECRET_KEY
from rest_framework import status
from django.http.response import JsonResponse

AUTH_HEADER_NAME = "HTTP_AUTHORIZATION"
AUTH_HEADER_TYPE = "Bearer"
INVALID_TOKEN = "invalid"
MISSING_TOKEN = "missing"
IDENTIFIER_CLAIM = "id"
EXPIRATION_CLAIM = "exp"
HS256 = "HS256"


def is_authorized():
    def decorator(function):
        def authorization_wrapper(self, *args, **kwargs):
            token = get_token(self.request)

            if token == MISSING_TOKEN:
                return JsonResponse({'message': 'Token não encontrado'}, status=status.HTTP_401_UNAUTHORIZED)

            if token == INVALID_TOKEN:
                return JsonResponse({'message': 'Token expirado ou inválido'}, status=status.HTTP_401_UNAUTHORIZED)

            return function(self, *args, **kwargs)

        return authorization_wrapper
    return decorator


def get_user(request) -> User:

    token = get_token(request)

    if token == MISSING_TOKEN or token == INVALID_TOKEN:
        return None

    try:
        return User.objects.get(pk=token[IDENTIFIER_CLAIM])
    except User.DoesNotExist:
        return None


def get_token(request) -> str:

    try:
        header = request.META.get(AUTH_HEADER_NAME)
        if header is None:
            return MISSING_TOKEN

        parts = header.split()

        if len(parts) == 0:
            return MISSING_TOKEN

        if len(parts) == 2:
            if parts[0] != AUTH_HEADER_TYPE:
                return MISSING_TOKEN

            token = parts[1]
        else:
            token = parts[0]

        validated_token = jwt.decode(token, SECRET_KEY, algorithms=[HS256])

        if not IDENTIFIER_CLAIM in validated_token:
            return INVALID_TOKEN

        return validated_token

    except Exception as e:
        return INVALID_TOKEN


def generate_token(user: User) -> str:

    encoded_jwt = jwt.encode(
        {IDENTIFIER_CLAIM: user.id,
         EXPIRATION_CLAIM: datetime.datetime.utcnow() + datetime.timedelta(seconds=600)
         }, SECRET_KEY, algorithm=HS256)
    return encoded_jwt


def hash_password(password: str) -> str:
    ph = PasswordHasher()
    return ph.hash(password)


def validate_password(password: str, hash: str) -> bool:
    ph = PasswordHasher()
    try:
        return ph.verify(hash, password)
    except:
        return False
