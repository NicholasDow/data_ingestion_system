from ingestion_pipeline.src.chunkers.fixedsize_chunker import FixedSizeChunker
# from ingestion_pipeline.src.embedders.pytorch_embedder import PyTorchEmbedder
# from ingestion_pipeline.src.embedders.tensorflow_embedder import TensorFlowEmbedder
from ingestion_pipeline.src.loaders import CSVLoader
from ingestion_pipeline.src.storage.dill_storage import DillDataStorage
from src.core.pipeline import Pipeline
from src.embedders.dummy_embedder import DummyEmbedder
from src.loaders.json_loader import JSONLoader

# maybe we can determine if we use json loader or a csv loader based on what we find in the blog
# Setup
loader = CSVLoader()
chunker = FixedSizeChunker(chunk_size=1024)
embedder = DummyEmbedder() # PyTorchEmbedder()
storage = DillDataStorage()

pipeline = Pipeline(loader, chunker, embedder, storage, data_home='./data_home')

# Process a new file
# When we process a dataset it should be given a title
pipeline.process('./sports', "sportsNews", title='title', text='content')

# We should be able to get all fo the
