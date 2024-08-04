from .base import DatasetFactory
from ..loaders.csv_loader import CSVLoader
from ..chunkers.simple_chunker import SimpleChunker

class CSVDatasetFactory(DatasetFactory):
    def create_loader(self):
        return CSVLoader()

    def create_chunker(self):
        return SimpleChunker()