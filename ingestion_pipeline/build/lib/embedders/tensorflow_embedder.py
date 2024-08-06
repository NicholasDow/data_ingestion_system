# from abc import ABC, abstractmethod
# from typing import List
# # import tensorflow as tf
# import tensorflow_hub as hub
#
# from ingestion_pipeline.src.embedders.base import Embedder
#
#
# class TensorFlowEmbedder(Embedder):
#     def __init__(self, model_url: str = "https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4"):
#         self.model = hub.load(model_url)
#
#     def embed(self, text: str) -> List[float]:
#         inputs = self.model.preprocessor([text])
#         outputs = self.model(inputs)
#         pooled_output = outputs["pooled_output"]
#         return pooled_output[0].numpy().tolist()