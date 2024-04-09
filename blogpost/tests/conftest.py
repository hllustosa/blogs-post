from __future__ import annotations

import os

import django
import pytest
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

django.setup()


@pytest.fixture
def client():
    from rest_framework.test import APIClient
    client = APIClient()
    return client


@pytest.fixture
def user_data():
    return {
        'displayName': 'Brett Wiltshire',
        'email': 'testemail@email.com',
        'password': '12345678',
        'image': 'http://4.bp.blogspot.com/_YA50adQ-7vQ/S1gfR_6ufpI/AAAAAAAAAAk/1ErJGgRWZDg/S45/brett.png',
    }


@pytest.fixture
def post_data():
    return {
        'title': 'Latest updates, August 1st',
        'content': 'The whole text for the blog post goes here in this key',
    }
