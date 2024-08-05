from typing import List
from .base import Embedder
from ..utils.decorators import log_operation


class DummyEmbedder(Embedder):
    # @log_operation
    def embed(self, text: str) -> List[float]:
        return [0.1] * 10  # Returns a 10-dimensional vector
