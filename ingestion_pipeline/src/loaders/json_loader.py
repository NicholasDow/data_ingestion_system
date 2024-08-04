import json
from typing import List
from .base import Loader
from ..core.document import Document
from ..utils.decorators import log_operation


class JSONLoader(Loader):
    @log_operation
    def load(self, file_path: str) -> List[Document]:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return [Document(str(i), "json_dataset", item.get('title', ''), item.get('text', ''), item)
                for i, item in enumerate(data)]

