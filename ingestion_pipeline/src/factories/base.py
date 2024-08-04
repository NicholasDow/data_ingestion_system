from abc import ABC, abstractmethod
from ..loaders.base import Loader
from ..chunkers.base import Chunker

class DatasetFactory(ABC):
    @abstractmethod
    def create_loader(self) -> Loader:
        pass

    @abstractmethod
    def create_chunker(self) -> Chunker:
        pass