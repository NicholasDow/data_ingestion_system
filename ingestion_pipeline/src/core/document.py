from typing import Dict, Any


# we might consider making date not a string so that we can organize the docs
class Document:
    def __init__(self, id: str, title: str, text: str, path: str, metadata: Dict[str, Any] = None):
        self.id = id
        # Didn't know if this was worth including or not
        # self.dataset = dataset
        # self.source_type = source_type
        self.title = title
        self.text = text
        self.path = path
        self.chunks = []
        self.metadata = metadata or {}

    def __repr__(self):
        return f"Document(id={self.id}, title={self.title[:20]}...)"
