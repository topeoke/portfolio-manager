import pytest
from src.portfolio.adapter.orm import start_mappers
from src.portfolio.config import Settings
from src.portfolio.adapter.repository import SessionFactory
from sqlalchemy.orm import clear_mappers


@pytest.fixture(name="env", autouse=True)
def fixture_env(monkeypatch):
    monkeypatch.setenv("database_url", "sqlite:///:memory/")
    monkeypatch.setenv("connection_args", "{}")


@pytest.fixture(name="start_end_mapper")
def fixture_start_end_mapper():
    start_mappers()
    yield
    clear_mappers()


@pytest.fixture(name="session")
def fixture_session(start_end_mapper):
    setting = Settings()
    factory = SessionFactory(setting)
    return factory()
