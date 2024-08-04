from typing import List
from ..loaders.base import Loader
from ..chunkers.base import Chunker
from ..embedders.base import Embedder
from ..storage.parquet_storage import ParquetStorage
from .document import Document
from ..utils.decorators import log_operation


class Pipeline:
    def __init__(self, loader: Loader, chunker: Chunker, embedder: Embedder):
        self.loader = loader
        self.chunker = chunker
        self.embedder = embedder

    @log_operation
    def process(self, file_path: str, output_path: str) -> None:
        documents = self.loader.load(file_path)
        chunks = []
        for doc in documents:
            doc_chunks = self.chunker.chunk(doc)
            for chunk in doc_chunks:
                chunk.embedding = self.embedder.embed(chunk.text)
            chunks.extend(doc_chunks)

        ParquetStorage.save_chunks(chunks, output_path)
        print(f"Processed and saved {len(chunks)} chunks to {output_path}")