from abc import ABC, abstractclassmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.portfolio.adapter.orm import metadata
from src.portfolio.domain import model
from src.portfolio.config import Settings
from typing import List


class AbstractRepository(ABC):
    @abstractclassmethod
    def add(self, portfolio: model.Portfolio):
        raise NotImplementedError

    @abstractclassmethod
    def get(self, id: str) -> model.Portfolio:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, portfolio: model.Portfolio):
        self.session.add(portfolio)

    def get(self) -> List[model.Portfolio]:
        return self.session.query(model.Portfolio).all()

    def get_by_id(self, id) -> model.Portfolio:
        return self.session.query(model.Portfolio).filter_by(id=id).first()

    def commit(self):
        self.session.commit()


class SessionFactory:
    """ session factory for database session"""

    def __init__(self, config: Settings):
        self.database_url = config.database_url
        self.connection_args = config.connection_args
        self.engine = create_engine(
            self.database_url, connect_args=self.connection_args
        )
        self.session_factory = sessionmaker(bind=self.engine)
        metadata.create_all(self.engine)

    def __call__(self, **kwargs):
        return self.session_factory(**kwargs)
