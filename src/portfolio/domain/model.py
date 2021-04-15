import attr
import uuid
from typing import List
from src.portfolio.domain.constants import AssetType, AssetCurrency


@attr.s
class Asset(object):
    id: uuid.UUID = attr.ib()
    ticker: str = attr.ib()
    name: str = attr.ib()
    qty: int = attr.ib()
    purchase_price: float = attr.ib()
    purchase_currency: AssetCurrency = attr.ib()
    asset_type: AssetType = attr.ib()
    asset_value: float = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.asset_value = self.qty * self.purchase_price

    @purchase_price.validator
    def check_price(self, attribute, price):
        if price <= 0:
            raise ValueError("Invalid price: Price must be greater than 0")
        return price

    @qty.validator
    def check_quantity(self, attribute, quantity):
        if quantity <= 0:
            raise ValueError(
                "Invalid Quantity: Asset quantity must be greater than 0"
            )
        return quantity


@attr.s
class Portfolio(object):
    id: uuid.UUID = attr.ib()
    version: int = attr.ib()
    portfolio_value: float = attr.ib(init=False)
    holdings: List[Asset] = attr.ib(factory=list)

    def __attrs_post_init__(self):
        self.portfolio_value = sum([i.asset_value for i in self.holdings])

    """
    @holdings.validator
    def check_holdings(self, attribute, asset_holdings):
        _holdings = list()
        for i in len(asset_holdings):
            for j in len(asset_holdings) - 1:
                if asset_holdings[j].ticker == asset_holdings[i].ticker:
                    _temp_asset = asset_holdings[i]
                    _temp_asset.qty = asset_holdings[j] + asset_holdings[i]
                    _holdings.append(_temp_asset)
    """
