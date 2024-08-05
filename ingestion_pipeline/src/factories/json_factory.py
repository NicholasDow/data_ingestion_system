from .base import DatasetFactory
from ..loaders.json_loader import JSONLoader
from ..chunkers.paragraph_chunker import ParagraphChunker

class JSONDatasetFactory(DatasetFactory):
    def create_loader(self):
        return JSONLoader()

    def create_chunker(self):
        return ParagraphChunker()