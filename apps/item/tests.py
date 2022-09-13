from decimal import Decimal

import pytest
from django.conf import settings
from django.test.client import Client

from apps.item import crud


# Create your tests here.
@pytest.mark.django_db
def test_get_item() -> None:
    item_data = crud.ItemCreateSchema(
        name="Item 1",
        price=Decimal(1111.23),
        description="Item description",
    )
    crud.item.create(data=item_data)
    item = crud.item.get(id_=1)
    assert item
    assert item.name == "Item 1"
    assert item.price == Decimal("1111.23")


@pytest.mark.django_db
def test_get_item_view(client: Client) -> None:
    item_data = crud.ItemCreateSchema(
        name="Item 1",
        price=Decimal(1111.23),
        description="Item description",
    )
    crud.item.create(data=item_data)
    response = client.get(f"{settings.CLIENT_BASE_URL}/item/1", follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_stripe_session(client: Client) -> None:
    item_data = crud.ItemCreateSchema(
        name="Item 1",
        price=Decimal(1111.23),
        description="Item description",
    )
    crud.item.create(data=item_data)
    response = client.get(f"{settings.CLIENT_BASE_URL}/buy/1", follow=True)
    result = response.json()
    assert response.status_code == 200
    assert result["id"].startswith("cs_test")
