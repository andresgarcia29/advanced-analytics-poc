from typing import List

from service import Service
from core import ProductsFilter
from entities import ProductOut


class Controller:
    def __init__(self) -> None:
        self.service = Service()

    def get_products_with_filters(self, filters: ProductsFilter) -> List[ProductOut]:
        return self.service.get_producs_with_filters(filters=filters)
