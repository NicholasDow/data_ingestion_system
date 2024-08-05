from abc import ABC, abstractmethod
from typing import Any


class DataStorage(ABC):
    @abstractmethod
    def save(self, data: Any, file_path: str) -> None:
        """Save data to a file."""
        pass

    @abstractmethod
    def load(self, file_path: str) -> Any:
        """Load data from a file."""
        pass