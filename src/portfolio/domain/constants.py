from enum import Enum


class AssetType(Enum):
    EQUITY = "Equity"
    CASH = "CASH"
    FIXEDINCOME = "FIXEDINCOME"


class AssetCurrency(Enum):
    GBP = "GBP"
    EURO = "EURO"
    USD = "USD"