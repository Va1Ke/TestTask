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
    req = {
    "dish_name": "onemorefood1"
    }
    response = client.post('/api/v1/dish/add/',req)
    data = response.data

    assert data["dish_name"] == req["dish_name"]

@pytest.mark.django_db
def test_get():
    response = client.get('/api/v1/menu-dish/list/')
    assert response.status_code == 200
