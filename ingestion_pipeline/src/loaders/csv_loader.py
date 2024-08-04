import csv
from typing import List
from .base import Loader
from ..core.document import Document
from ..utils.decorators import log_operation


class CSVLoader(Loader):
    @log_operation
    def load(self, file_path: str) -> List[Document]:
        documents = []
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                documents.append(Document(str(i), "csv_dataset", row.get('title', ''), row.get('text', ''), row))
        return documents
