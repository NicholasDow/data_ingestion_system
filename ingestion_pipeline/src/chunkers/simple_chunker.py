from typing import List
from .base import Chunker
from ..core.document import Document
from ..core.chunk import Chunk
from ..utils.decorators import log_operation

class SimpleChunker(Chunker):
    @log_operation
    def chunk(self, document: Document) -> List[Chunk]:
        paragraphs = document.text.split('\n\n')
        return [Chunk(f"{document.id}_{i}", document.id, para)
                for i, para in enumerate(paragraphs)]