from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    Enum,
)
from sqlalchemy.orm import mapper, relationship
from sqlalchemy_utils import UUIDType
from src.portfolio.domain.constants import AssetCurrency, AssetType
from src.portfolio.domain import model

metadata = MetaData()

assets = Table(
    "assets",
    metadata,
    Column("id", UUIDType(binary=False), primary_key=True),
    Column("name", String),
    Column("ticker", String),
    Column("qty", Integer),
    Column("purchase_price", Float),
    Column("purchase_currency", Enum(AssetCurrency)),
    Column("asset_type", Enum(AssetType)),
    Column("asset_value", Float),
    Column("portfolio_id", ForeignKey("portfolio.id")),
)

portfolio = Table(
    "portfolio",
    metadata,
    Column("id", UUIDType(binary=False), primary_key=True),
    Column("portfolio_value", Float),
    Column("version", Integer, nullable=False),
)


def start_mappers():
    asset_mapper = mapper(model.Asset, assets)
    mapper(
        model.Portfolio,
        portfolio,
        properties={
            "holdings": relationship(asset_mapper, collection_class=list),
        },
        version_id_col=portfolio.c.version,
    )
