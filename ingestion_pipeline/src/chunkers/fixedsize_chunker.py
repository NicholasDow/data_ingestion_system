import textwrap
from typing import List

from ingestion_pipeline.src.chunkers.base import Chunker
from ingestion_pipeline.src.core.document import Document
from ingestion_pipeline.src.core.chunk import Chunk
from ingestion_pipeline.src.utils import log_operation


# there something with white space that we need to consider with this one
class FixedSizeChunker(Chunker):
    def __init__(self, chunk_size: int):
        self.chunk_size = chunk_size

    @log_operation
    def chunk(self, document: Document) -> List[Chunk]:
        # Use textwrap to split the text into chunks of approximately chunk_size characters
        chunks = textwrap.wrap(document.text, width=self.chunk_size, break_long_words=False, replace_whitespace=False)

        return [Chunk(f"{document.id}_{i}", document.id, chunk)
                for i, chunk in enumerate(chunks)]