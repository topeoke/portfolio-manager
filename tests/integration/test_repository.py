from tests.helper import Asset_Generator
from src.portfolio.domain import model
from src.portfolio.adapter.repository import SqlAlchemyRepository
import uuid


def test_portfolio_add(session):
    """ testing repository """
    assets = [Asset_Generator() for _ in range(3)]
    portfolio_ = model.Portfolio(id=uuid.uuid4(), version=100, holdings=assets)
    assert isinstance(portfolio_.id, uuid.UUID)
    repo = SqlAlchemyRepository(session)
    repo.add(portfolio_)
    repo.commit
    result = repo.get_by_id(portfolio_.id)
    assert isinstance(result.version, int)
    assert isinstance(result.id, uuid.UUID)
    assert isinstance(result.holdings[0], model.Asset)
    assert result.portfolio_value == sum(
        [i.asset_value for i in result.holdings]
    )
