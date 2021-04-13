import attr
import uuid
from typing import List
from portfolio.domain.constants import AssetType, AssetCurrency


@attr.s
class Asset(object):
    id: uuid.UUID = attr.ib()
    ticker: str = attr.ib()
    name: str = attr.ib()
    qty: int = attr.ib()
    purchase_price: float = attr.ib()
    purchase_currency: AssetCurrency = attr.ib()
    asset_type: AssetType = attr.ib()

    @purchase_price.validator
    def check_price(self, attribute, price):
        if price <= 0 :
            raise ValueError("Invalid price: Price must be greater than 0")
        return price
    
    @qty.validator
    def check_quantity(self, attribute, quantity):
        if quantity <= 0 :
            raise ValueError("Invalid Quantity: Asset quantity must be greater than 0")
        return quantity

@attr.s
class Portfolio(object):
    id: uuid.UUID = attr.ib()
    holdings: List[Asset] = attr.ib(factory=list)
    version: int = attr.ib()
