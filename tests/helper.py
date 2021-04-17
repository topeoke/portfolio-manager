from src.portfolio.domain import model, constants
import string
import random
import uuid


def Asset_Generator() -> model.Asset:
    """ Retrun an asset object"""
    test_ticker = "".join(
        random.choice(string.ascii_uppercase) for i in range(3)
    )
    test_qty = (
        int("".join(random.choice(string.digits) for i in range(3))) + 10
    )
    test_price = (
        float("".join(random.choice(string.digits) for i in range(3))) + 10
    )

    return model.Asset(
        id=uuid.uuid4(),
        ticker=test_ticker,
        name=str(uuid.uuid4()),
        qty=test_qty,
        purchase_price=test_price,
        purchase_currency=constants.AssetCurrency.GBP,
        asset_type=constants.AssetType.EQUITY,
    )
