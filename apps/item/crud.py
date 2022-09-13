from dataclasses import dataclass
from decimal import Decimal

from apps.common.crud import BaseCRUD

from .models import Item


@dataclass
class ItemCreateSchema:
    name: str
    price: Decimal
    description: str


class ItemCRUD(BaseCRUD[Item, ItemCreateSchema]):
    """Item CRUD services"""


item = ItemCRUD(Item)
