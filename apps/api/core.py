from pydantic import BaseModel


class HealthCheck(BaseModel):
    message: str


class ProductsFilter(BaseModel):
    costs: str = ""
    greater: bool = False
    less: bool = False
