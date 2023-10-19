from typing import List

from repository import Repository

from entities import ProductOut
from core import ProductsFilter


class Service:
    def __init__(self) -> None:
        self.repository = Repository()

    def get_producs_with_filters(self, filters: ProductsFilter) -> List[ProductOut]:
        return self.repository.get_products(filters=filters)
