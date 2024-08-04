import pyarrow as pa
import pyarrow.parquet as pq
from typing import List
from ..core import Chunk


class ParquetStorage:
    @staticmethod
    def save_chunks(chunks: List[Chunk], file_path: str):
        data = {
            'id': [chunk.id for chunk in chunks],
            'doc_id': [chunk.doc_id for chunk in chunks],
            'text': [chunk.text for chunk in chunks],
            'embedding': [chunk.embedding for chunk in chunks]
        }
        table = pa.Table.from_pydict(data)
        pq.write_table(table, file_path)

    @staticmethod
    def load_chunks(file_path: str) -> pa.Table:
        return pq.read_table(file_path)