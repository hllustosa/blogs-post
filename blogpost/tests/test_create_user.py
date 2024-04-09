from __future__ import annotations

import json

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_user(client, user_data):
    url = reverse('users:create-user')
    response = client.post(
        url, data=json.dumps(
            user_data,
        ), content_type='application/json',
    )
    assert response.status_code == 201
    assert 'token' in response.json()


@pytest.mark.django_db
def test_invalid_display_name(client, user_data):
    user_data['displayName'] = 'Rubens'
    url = reverse('users:create-user')
    response = client.post(
        url, data=json.dumps(
            user_data,
        ), content_type='application/json',
    )
    assert response.status_code == 400
    assert response.json()[
        'message'
    ] == '"displayName" length must be at least 8 characters long'


@pytest.mark.django_db
def test_invalid_email(client, user_data):
    user_data['email'] = 'invalidemail'
    url = reverse('users:create-user')
    response = client.post(
        url, data=json.dumps(
            user_data,
        ), content_type='application/json',
    )
    assert response.status_code == 400
    assert response.json()['message'] == '"email" must be a valid email'
