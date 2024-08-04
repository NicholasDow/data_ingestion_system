from typing import Dict, Any


class Document:
    def __init__(self, id: str, dataset: str, title: str, text: str, metadata: Dict[str, Any] = None):
        self.id = id
        self.dataset = dataset
        self.title = title
        self.text = text
        self.metadata = metadata or {}

    def __repr__(self):
        return f"Document(id={self.id}, dataset={self.dataset}, title={self.title[:20]}...)"
