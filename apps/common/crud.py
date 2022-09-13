from dataclasses import asdict
from typing import Generic, Optional, Protocol, Type, TypeVar

from django.db.models import Model


class BaseSchema(Protocol):
    """Base Schema"""


ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseSchema)


class BaseCRUD(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, id_: int) -> Optional[ModelType]:
        try:
            result = self.model.objects.get(pk=id_)
        except self.model.DoesNotExist:
            return None
        else:
            return result

    def create(self, data: CreateSchemaType) -> Optional[ModelType]:
        return self.model.objects.create(**asdict(data))
