from typing import List

from fastapi import APIRouter

from controller import Controller
from core import ProductsFilter
from entities import ProductOut
from messages import ERROR_404

router = APIRouter(prefix="/products", tags=["product"], responses={404: ERROR_404})
controller = Controller()


@router.get("")
async def get_products(
    costs: str = "0", greater: str = "0", less: str = "0"
) -> List[ProductOut]:
    return controller.get_products_with_filters(
        filters=ProductsFilter(costs=costs, greater=greater, less=less)
    )
