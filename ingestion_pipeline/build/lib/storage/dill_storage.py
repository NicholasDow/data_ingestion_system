from typing import Any
import dill

from ingestion_pipeline.src.storage.base import DataStorage


class DillDataStorage(DataStorage):
    extension = 'dill'
    def save(self, data: Any, file_path: str) -> None:
        """Save data to a file using dill."""
        with open(file_path, 'wb') as f:
            dill.dump(data, f)

    def load(self, file_path: str) -> Any:
        """Load data from a file using dill."""
        with open(file_path, 'rb') as f:
            return dill.load(f)