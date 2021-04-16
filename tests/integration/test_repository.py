from tests.helper import Asset_Generator
from src.portfolio.domain.model import Portfolio
import uuid
import pytest


pytestmark = pytest.mark.usefixtures("mappers")


def test_portfolio_add(sqlite_session_factory):
    assets = [Asset_Generator() for _ in range(3)]
    portfolio_ = Portfolio(id=uuid.uuid4(), version=100, holdings=assets)
    assert isinstance(portfolio_.id, uuid.UUID)
    # repo = SqlAlchemyRepository(session)
    # repo.add(portfolio)
    # repo.commit
    # result = repo.get_by_id(portfolio.id)
    # assert isinstance(result.holdings[0], Asset)
