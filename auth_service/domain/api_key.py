from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class APIKeyAccessLevelEnum(StrEnum):
    READ = "read"
    WRITE = "write"


@dataclass
class APIKey:
    key: str
    access_level: APIKeyAccessLevelEnum
    created_at: datetime
    status: str
    last_accessed: datetime
