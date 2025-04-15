from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class AccessLevelEnum(StrEnum):
    READ = "read"
    WRITE = "write"


@dataclass
class APIKey:
    key: str
    access_level: AccessLevelEnum
    created_at: datetime
    last_accessed: datetime
