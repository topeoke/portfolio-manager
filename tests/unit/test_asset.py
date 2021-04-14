from tests.helper import Asset_Generator
from src.portfolio.domain.constants import AssetType
from src.portfolio.domain.model import Portfolio, Asset
import uuid
from typing import List


def test_portfolio_asset():
    asset = Asset_Generator()
    assert isinstance(asset.id, uuid.UUID)


def test_asset_value():
    asset = Asset_Generator()
    assert asset.asset_value == asset.qty * asset.purchase_price


def test_multiple_assets():
    assets = [Asset_Generator() for i in range(10)]
    for asset in assets:
        assert isinstance(asset.ticker, str)
        assert isinstance(asset.asset_type, AssetType)


def test_portfolio():
    assets = [Asset_Generator() for i in range(10)]
    asset_sum = sum([i.asset_value for i in assets])
    portfolio = Portfolio(
                id = uuid.uuid4(),
                version = 1,
                holdings = assets
    )
    assert isinstance(portfolio.holdings[0], Asset)
    assert asset_sum == portfolio.portfolio_value