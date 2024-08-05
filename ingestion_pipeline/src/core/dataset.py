from datetime import datetime
from typing import Dict, List, Any

# from .operation import Operation
from ingestion_pipeline.src.core.document import Document

# The datasets come in varied formats, we are given one dataset which is a list of csv or a folder of jsons.
class Dataset:
    def __init__(self, title: str, url: str, documents: List[Document], metadata: Dict[str, Any] = None):
        # we should basically check if in our system there is a dataset with the same title and remove the data at
        # the end of writing the new data

        self.title = title
        self.date_created = datetime.today()
        self.url = url
        # these are the docs when first read in
        self.raw_documents = documents
        # these are the docs after operations
        self.documents = documents
        # self.operations: List[Operation] = []
        # this is honestly just additional data that we might want to add to the dataset. I think we might consider
        # making this a json that is read from the folder containing the data
        self.metadata = metadata or {}

    def __repr__(self):
        return f"Dataset(title={self.title}, documents={self.documents}, metadata={self.metadata}...)"
