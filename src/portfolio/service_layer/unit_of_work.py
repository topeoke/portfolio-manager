from abc import ABC, abstractmethod
from src.portfolio.adapter import repository


class AbstractUnitOfWork(ABC):
    """ Abstract Unit of Work """

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    """ Unit of work for sqlalchemy """

    def __init__(self, session_factory):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.portfolio = repository.SqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
