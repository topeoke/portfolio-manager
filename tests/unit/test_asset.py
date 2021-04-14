from tests.helper import Asset_Generator
import uuid


def test_portfolio_asset():
    asset = Asset_Generator()
    assert isinstance(asset.id, uuid.UUID)
