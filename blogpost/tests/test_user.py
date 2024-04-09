from __future__ import annotations

import json

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_user(client, user_data):
    status_code, response = call_create_user(client, user_data)

    for field in ['displayName', 'email', 'image']:
        assert response[field] == user_data[field]

    assert status_code == 201


@pytest.mark.django_db
def test_create_user_with_duplicated_email(client, user_data):
    status_code, _ = call_create_user(client, user_data)
    assert status_code == 201

    status_code, response = call_create_user(client, user_data)
    assert status_code == 400
    assert response['non_field_errors'] == ['User already exists']


@pytest.mark.parametrize('field', ['displayName', 'password', 'email'])
@pytest.mark.django_db
def test_create_user_with_missing_required_fields(client, user_data, field):
    del user_data[field]
    status_code, response = call_create_user(client, user_data)

    assert status_code == 400
    assert response[
        field
    ] == ['This field is required.']


@pytest.mark.parametrize(
    'field, invalid', [
        ('password', '123'),
        ('email', 'invalid'),
    ],
)
@pytest.mark.django_db
def test_create_user_with_invalid_fields_values(client, user_data, field, invalid):
    user_data[field] = invalid
    status_code, response = call_create_user(client, user_data)

    assert status_code == 400
    assert field in response


def call_create_user(client, user_data):
    url = reverse('users:create-user')
    response = client.post(
        url, data=json.dumps(
            user_data,
        ), content_type='application/json',
    )
    return response.status_code, response.json()
