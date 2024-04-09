from __future__ import annotations

import json

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_post(client, user_data, post_data):
    status_code, response = call_create_post(client, user_data, post_data)

    for field in ['title', 'content']:
        assert response[field] == post_data[field]

    assert status_code == 201


@pytest.mark.parametrize('field', ['title', 'content'])
@pytest.mark.django_db
def test_create_post_with_missing_required_fields(client, user_data, post_data, field):
    del post_data[field]
    status_code, response = call_create_post(client, user_data, post_data)

    assert status_code == 400
    assert response[
        field
    ] == ['This field is required.']


def call_create_post(client, user_data, post_data):
    url = reverse('users:create-user')
    response = client.post(
        url, data=json.dumps(
            user_data,
        ), content_type='application/json',
    )

    url = reverse('users:login')
    response = client.post(
        url, data=json.dumps({
            'email': user_data['email'],
            'password': user_data['password'],
        }), content_type='application/json',
    )
    token = response.json()['token']

    url = reverse('posts:list-create')
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = client.post(
        url, data=json.dumps(
            post_data,
        ), content_type='application/json',
    )
    return response.status_code, response.json()
