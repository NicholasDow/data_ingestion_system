import os
from pathlib import Path
from typing import List

from .dataset import Dataset
from ..loaders.base import Loader
from ..chunkers.base import Chunker
from ..embedders.base import Embedder
from ..storage.dill_storage import DataStorage as Storage
from ..utils.decorators import log_operation


class Pipeline:
    def __init__(self, loader: Loader, chunker: Chunker, embedder: Embedder, data_home: str = None):
        self.loader = loader
        self.chunker = chunker
        self.embedder = embedder

        # Set data_home to the provided path or default to './data'
        self.data_home = Path(data_home) if data_home else Path.cwd() / 'data'

        # Ensure the data_home directory exists
        self.data_home.mkdir(parents=True, exist_ok=True)

        # Create input_home folder within data_home
        self.input_home = self.data_home / 'input_home'
        self.input_home.mkdir(parents=True, exist_ok=True)

    @log_operation
    def process(self, input_folder: str, title: str) -> None:
        input_path = self.input_home / input_folder
        if not input_path.exists():
            raise FileNotFoundError(f"Input folder {input_path} does not exist in input_home.")

        documents = self.loader.load(str(input_path))
        for doc in documents:
            doc_chunks = self.chunker.chunk(doc)
            for chunk in doc_chunks:
                chunk.embedding = self.embedder.embed(chunk.text)
            doc.chunks = doc_chunks

        dataset = Dataset(title, '', documents)

        # Check if dataset already exists and remove if it does
        if self.dataset_exists(title):
            self.remove_existing_dataset(title)
            print(f"Removed existing dataset: {title}")

        Storage.save(dataset)
        print(f"Processed and saved dataset: {title}")

    def get_data_home(self) -> str:
        return str(self.data_home)

    def list_datasets(self) -> List[str]:
        return [f.stem for f in self.data_home.glob('*.dill')]

    def dataset_exists(self, title: str) -> bool:
        return (self.data_home / f"{title}.dill").exists()

    def remove_existing_dataset(self, title: str) -> None:
        dataset_file = self.data_home / f"{title}.dill"
        if dataset_file.exists():
            dataset_file.unlink()