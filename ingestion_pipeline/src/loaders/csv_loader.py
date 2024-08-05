import csv
from typing import List
from .base import Loader
from ..core.document import Document
from ..utils.decorators import log_operation

import csv
import os
from typing import List
from pathlib import Path


class CSVLoader(Loader):
    @log_operation
    def load(self, directory_path: str, title: str = 'title', text: str = 'text') -> List[Document]:
        documents = []
        directory = Path(directory_path)

        for file_path in directory.rglob('*.csv'):
            with open(file_path, 'r', newline='', encoding='utf-8') as f:
                try:
                    # could use pandas or dask here should allow for this to be switched out
                    csv_reader = csv.DictReader(f)
                    for i, row in enumerate(csv_reader):
                        # Assume 'title' and 'text' columns exist, otherwise use empty strings
                        title = row.get(title, '')
                        text = row.get(text, '')

                        # If 'title' or 'text' don't exist, we might want to create a text
                        # representation of the entire row
                        # brute force solution
                        if not (title or text):
                            text = ', '.join(f"{k}: {v}" for k, v in row.items())

                        doc_id = f"{file_path.stem}_{i}"
                        doc = Document(
                            id=doc_id,
                            title=title,
                            text=text,
                            path=str(file_path)
                        )
                        documents.append(doc)
                except csv.Error as e:
                    print(f"Error reading CSV file {file_path}: {e}")

        return documents
