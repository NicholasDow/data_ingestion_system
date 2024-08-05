from .base import DatasetFactory
from ..loaders.csv_loader import CSVLoader
from ..chunkers.paragraph_chunker import ParagraphChunker

class CSVDatasetFactory(DatasetFactory):
    def create_loader(self):
        return CSVLoader()

    def create_chunker(self):
        return ParagraphChunker()