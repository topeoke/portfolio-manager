import pytest
from src.portfolio.adapter.orm import start_mappers, metadata


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

"""

@pytest.fixture(name='env', autouse=True)
def fixture_env(monkeypatch):
    monkeypatch.setenv('database_url', 'sqlite:///:memory/')
    monkeypatch.setenv('connection_args', '{}')


@pytest.fixture(name='start_end_mapper')
def fixture_start_end_mapper():
    start_mappers()
    yield
    clear_mappers()

@pytest.fixture(name='session')
def fixture_session(start_end_mapper):
    setting = Settings(database_url='sqlite:///:memory/')
    factory = SessionFactory(setting)
    return factory()


"""


@pytest.fixture
def in_memory_sqlite_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def sqlite_session_factory(in_memory_sqlite_db):
    yield sessionmaker(bind=in_memory_sqlite_db)


@pytest.fixture
def mappers():
    start_mappers()
    yield
    clear_mappers()
