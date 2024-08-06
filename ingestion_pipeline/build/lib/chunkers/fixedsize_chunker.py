import textwrap
from typing import List

from ingestion_pipeline.src.chunkers.base import Chunker
from ingestion_pipeline.src.core.document import Document
from ingestion_pipeline.src.core.chunk import Chunk
from ingestion_pipeline.src.utils import log_operation

# This treats white space as a single space pretty much ignoring it.
# I've noticed that there are a lot of headers that are redundant and should be cleaned out of the data
class FixedSizeChunker(Chunker):
    def __init__(self, chunk_size: int):
        self.chunk_size = chunk_size

    # @log_operation
    def chunk(self, document: Document) -> List[Chunk]:
        # Use textwrap to split the text into chunks of approximately chunk_size characters
        chunks = textwrap.wrap(document.text, width=self.chunk_size, break_long_words=True, replace_whitespace=False)

        return [Chunk(f"{document.id}_{i}", document.id, chunk)
                for i, chunk in enumerate(chunks)]