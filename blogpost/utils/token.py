from __future__ import annotations

import datetime

import jwt
from apps.users.models import User
from settings import SECRET_KEY

AUTH_HEADER_NAME = 'HTTP_AUTHORIZATION'
AUTH_HEADER_TYPE = 'Bearer'
IDENTIFIER_CLAIM = 'id'
EXPIRATION_CLAIM = 'exp'
HS256 = 'HS256'


def get_token(request):

    try:

        header = request.META.get(AUTH_HEADER_NAME)

        if header is None:
            return None

        parts = header.split()

        if len(parts) == 0:
            return None

        if len(parts) == 2:

            if parts[0] != AUTH_HEADER_TYPE:
                return None

            token = parts[1]
        else:
            token = parts[0]

        validated_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        if IDENTIFIER_CLAIM not in validated_token:
            return None

        return validated_token

    except Exception:
        return None


def generate_token(user: User) -> str:

    encoded_jwt = jwt.encode(
        {
            IDENTIFIER_CLAIM: user.id,
            EXPIRATION_CLAIM: datetime.datetime.utcnow() + datetime.timedelta(seconds=600),
        }, SECRET_KEY, algorithm=HS256,
    )

    return str(encoded_jwt)


def get_user_id(request) -> str | None:

    token = get_token(request)

    if token is None:
        return None

    return token[IDENTIFIER_CLAIM]
