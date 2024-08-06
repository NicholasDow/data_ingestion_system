import re
from typing import List

from ingestion_pipeline.src.chunkers.base import Chunker
from ingestion_pipeline.src.core import Document, Chunk
from ingestion_pipeline.src.utils import log_operation


class SentenceChunker(Chunker):
    @log_operation
    def chunk(self, document: Document) -> List[Chunk]:
        # Split the text into sentences
        sentences = re.split(r'(?<=[.!?])\s+', document.text)

        return [Chunk(f"{document.id}_{i}", document.id, sentence)
                for i, sentence in enumerate(sentences)]