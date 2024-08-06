from typing import List


class Chunk:
    def __init__(self, id: str, doc_id: str, text: str, embedding: List[float] = None):
        self.id = id
        self.doc_id = doc_id
        self.text = text
        self.embedding = embedding

    def __repr__(self):
        return f"Chunk(id={self.id}, doc_id={self.doc_id}, text={self.text[:20]}...)"
