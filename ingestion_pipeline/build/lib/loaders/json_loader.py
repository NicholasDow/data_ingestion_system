import json
from typing import List
from .base import Loader
from ..core.document import Document
from ..utils.decorators import log_operation


import json
import os
from typing import List
from pathlib import Path

class JSONLoader(Loader):
    @log_operation
    def load(self, directory_path: str, title: str = 'title', text: str = 'text') -> List[Document]:
        documents = []
        directory = Path(directory_path)

        for file_path in directory.rglob('*.json'):
            with open(file_path, 'r') as f:
                try:
                    data = json.load(f)
                    # jsons can be arrays
                    if isinstance(data, list):
                        for i, item in enumerate(data):
                            doc_id = f"{file_path.stem}_{i}"
                            doc = Document(
                                id=doc_id,
                                # source_type="json_dataset",
                                title=item.get(title, ''),
                                text=item.get(text, ''),
                                path=str(file_path)
                            )
                            documents.append(doc)
                    elif isinstance(data, dict):
                        doc = Document(
                            id=file_path.stem,
                            # source_type="json_dataset",
                            title=data.get(title, ''),
                            text=data.get(text, ''),
                            path=str(file_path)
                        )
                        documents.append(doc)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON file: {file_path}")

        return documents

