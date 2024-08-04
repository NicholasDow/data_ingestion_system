from .base import DatasetFactory
from ..loaders.json_loader import JSONLoader
from ..chunkers.simple_chunker import SimpleChunker

class JSONDatasetFactory(DatasetFactory):
    def create_loader(self):
        return JSONLoader()

    def create_chunker(self):
        return SimpleChunker()