from abc import ABC, abstractmethod
from typing import List
from ..core.document import Document
from ..core.chunk import Chunk


class Chunker(ABC):
    @abstractmethod
    def chunk(self, document: Document) -> List[Chunk]:
        pass
