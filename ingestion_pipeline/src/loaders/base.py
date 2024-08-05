from abc import ABC, abstractmethod
from typing import List
from ..core.document import Document


class Loader(ABC):
    @abstractmethod
    def load(self, file_path: str, title: str, text: str) -> List[Document]:
        pass
