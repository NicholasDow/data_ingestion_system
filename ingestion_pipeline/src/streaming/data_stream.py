import asyncio
from typing import AsyncIterator, Dict, Any

class DataStream:
    def __init__(self):
        self.queue = asyncio.Queue()

    async def push(self, data: Dict[str, Any]):
        await self.queue.put(data)

    async def get(self) -> AsyncIterator[Dict[str, Any]]:
        while True:
            try:
                yield await self.queue.get()
            except asyncio.CancelledError:
                break

data_stream = DataStream()