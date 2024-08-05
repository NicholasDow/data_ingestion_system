from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import Dict, Any

from ..streaming.data_stream import DataStream
from ..core.pipeline import Pipeline
from ..loaders.json_loader import JSONLoader
from ..chunkers.paragraph_chunker import ParagraphChunker
from ..embedders.dummy_embedder import DummyEmbedder

app = FastAPI()

# Initialize components
data_stream = DataStream()
loader = JSONLoader()
chunker = ParagraphChunker()
embedder = DummyEmbedder()
pipeline = Pipeline(loader, chunker, embedder)

class StreamData(BaseModel):
    data: Dict[str, Any]

@app.post("/stream")
async def receive_stream(stream_data: StreamData):
    await data_stream.push(stream_data.data)
    return {"status": "received"}

@app.get("/process")
async def process_stream(background_tasks: BackgroundTasks):
    background_tasks.add_task(process_stream_data)
    return {"status": "processing started"}

async def process_stream_data():
    async for data in data_stream.get():
        document = loader.load_from_dict(data)
        chunks = chunker.chunk(document)
        for chunk in chunks:
            chunk.embedding = embedder.embed(chunk.text)
