from src.portfolio.service_layer import unit_of_work
from tests.helper import Asset_Generator
from src.portfolio.domain.model import Portfolio
from src.portfolio.adapter.repository import SessionFactory
from src.portfolio.config import Settings
import uuid

# pytestmark = pytest.mark.usefixtures('start_end_mapper')


def test_uow(start_end_mapper):
    config = Settings()
    print(config.database_url)
    factory = SessionFactory(config)
    asset = Asset_Generator()
    uow = unit_of_work.SqlAlchemyUnitOfWork(factory)
    port_ = Portfolio(id=uuid.uuid4(), version=1, holdings=[asset])
    with uow:
        uow.portfolio.add(port_)
        result = uow.session.query(Portfolio).filter_by(id=port_.id).first()
        uow.commit()
        assert isinstance(result.id, uuid.UUID)
        assert result.version == 1
        assert result.portfolio_value == asset.asset_value
