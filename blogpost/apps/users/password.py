from __future__ import annotations

from argon2 import PasswordHasher


def hash_password(password: str) -> str:
    ph = PasswordHasher()
    return ph.hash(password)


def validate_password(password: str, hash: str) -> bool:
    ph = PasswordHasher()
    try:
        return ph.verify(hash, password)
    except Exception:
        return False
