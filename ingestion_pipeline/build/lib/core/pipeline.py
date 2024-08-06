import os
from pathlib import Path
from typing import List

from .dataset import Dataset
from ..loaders.base import Loader
from ..chunkers.base import Chunker
from ..embedders.base import Embedder
from ..storage.dill_storage import DataStorage
from ..utils.decorators import log_operation


class Pipeline:
    def __init__(self, loader: Loader, chunker: Chunker, embedder: Embedder, storage: DataStorage, data_home: str = None):
        self.loader = loader
        self.chunker = chunker
        self.embedder = embedder
        self.storage = storage

        # Set data_home to the provided path or default to './data'
        self.data_home = Path(data_home) if data_home else Path.cwd() / 'data'
        # Ensure the data_home directory exists
        self.data_home.mkdir(parents=True, exist_ok=True)

        # Create input_home folder within data_home
        self.input_home = self.data_home / 'input_home'
        self.input_home.mkdir(parents=True, exist_ok=True)
        self.storage_location = self.data_home / self.storage.extension
        self.storage_location.mkdir(parents=True, exist_ok=True)


    @log_operation
    def process(self, input_folder: str, name: str, overwrite: bool, title: str = 'title', text: str = 'text') -> None:
        input_path = self.input_home / input_folder
        if not input_path.exists():
            raise FileNotFoundError(f"Input folder {input_path} does not exist in input_home.")

        # If we use the wrong loader then we get an empty doc, we should keep the loaders separate but still
        documents = self.loader.load(str(input_path), title, text)
        if documents == []:
            raise IOError(f"Loader {self.loader} likely incorrect loader, no documents found")
        for doc in documents:
            doc_chunks = self.chunker.chunk(doc)
            for chunk in doc_chunks:
                chunk.embedding = self.embedder.embed(chunk.text)
            doc.chunks = doc_chunks

        dataset = Dataset(name, '', documents)

        # Check if dataset already exists and remove if it does
        if self.dataset_exists(name) and overwrite:
            self.remove_existing_dataset(name)
            print(f"Removed existing dataset: {name}")

        dataset_save_location = self.storage_location / f"{name}.{self.storage.extension}"
        self.storage.save(data=dataset, file_path=dataset_save_location)
        print(f"Processed and saved dataset: {name}")

    def get_data_home(self) -> str:
        return str(self.data_home)

    def list_datasets(self) -> List[str]:
        return [f.stem for f in self.storage_location.glob(f"*.{self.storage.extension}")]

    def dataset_exists(self, name: str) -> bool:
        return (self.storage_location / f"{name}.{self.storage.extension}").exists()

    def remove_existing_dataset(self, name: str) -> None:
        dataset_file = self.storage_location / f"{name}.{self.storage.extension}"
        if dataset_file.exists():
            dataset_file.unlink()
