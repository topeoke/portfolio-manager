from pydantic import BaseSettings
from typing import Dict, Optional


class Settings(BaseSettings):
    """ Configuration Settings """

    database_url: Optional[str]
    connection_args: Optional[Dict]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
