import pytest
from rest_framework.test import APIClient

from api.models import User

client = APIClient()

@pytest.mark.django_db
def test_my_user():
    me = User.objects.get(username='me')
    assert me.is_superuser

@pytest.mark.django_db
def test_post():
    payload = {
    "dish_name": "onemorefood1"
    }
    response = client.post('/api/v1/dish/add/',payload)
    data = response.data

    assert data["dish_name"] == payload["dish_name"]
