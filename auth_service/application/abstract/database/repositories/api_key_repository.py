from abc import abstractmethod
from typing import Protocol


class ApiKeyRepository(Protocol):
    @abstractmethod
    def is_allowed_to_read(self, key_id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_allower_to_write(self, key_id: str) -> bool:
        raise NotImplementedError
