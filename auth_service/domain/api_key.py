from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum

from auth_service.domain.api_key_id import ApiKeyId


class APIKeyAccessLevelEnum(StrEnum):
    READ = "read"
    WRITE = "write"


class APIKeyStatusEnum(StrEnum):
    ACTIVE = "active"
    REVOKED = "revoked"
    EXPIRED = "expired"


@dataclass
class APIKey:
    key_id: ApiKeyId | None
    key: str
    access_level: APIKeyAccessLevelEnum
    status: APIKeyStatusEnum
    created_at: datetime
    last_accessed: datetime
