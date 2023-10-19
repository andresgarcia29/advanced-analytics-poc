from pydantic import BaseModel


class ProductOut(BaseModel):
    name: str
    cost: int
    description: str
