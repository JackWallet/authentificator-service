from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager
from typing import Generic, TypeVar

SessionType = TypeVar("SessionType")


class Database(ABC, Generic[SessionType]):
    @abstractmethod
    def get_session(self) -> AbstractAsyncContextManager[SessionType]:
        raise NotImplementedError

    @abstractmethod
    async def dispose(self) -> None:
        raise NotImplementedError
