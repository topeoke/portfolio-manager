from src.portfolio.service_layer import unit_of_work
from tests.helper import Asset_Generator
from src.portfolio.domain.model import Portfolio
from src.portfolio.adapter.repository import SessionFactory
from src.portfolio.config import Settings
import uuid


def test_uow(start_end_mapper):
    config = Settings()
    factory = SessionFactory(config)
    assets = [Asset_Generator() for i in range(150)]
    total = sum([i.asset_value for i in assets])
    uow = unit_of_work.SqlAlchemyUnitOfWork(factory)
    port_ = Portfolio(id=uuid.uuid4(), version=1, holdings=assets)
    with uow:
        uow.portfolio.add(port_)
        result = uow.portfolio.get_by_id(port_.id)
        uow.commit()
        assert isinstance(result.id, uuid.UUID)
        assert result.version == 1
        assert result.portfolio_value == total
