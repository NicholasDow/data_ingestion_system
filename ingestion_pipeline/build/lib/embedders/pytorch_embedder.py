# from typing import List
#
# import torch
# from transformers import BertModel, BertTokenizer
# import numpy as np
#
# from ingestion_pipeline.src.embedders.base import Embedder
#
#
# class PyTorchEmbedder(Embedder):
#     def __init__(self, model_name: str = 'bert-base-uncased', max_length: int = 1024, stride: int = 1024):
#         self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#         self.tokenizer = BertTokenizer.from_pretrained(model_name)
#         self.model = BertModel.from_pretrained(model_name).to(self.device)
#         self.model.eval()
#         self.max_length = max_length
#         self.stride = stride
#
#     def embed(self, text: str) -> List[float]:
#         # Tokenize the input text
#         tokens = self.tokenizer.tokenize(text)
#
#         # If the text is shorter than max_length, process it directly
#         if len(tokens) <= self.max_length:
#             return self._embed_chunk(text)
#
#         # For longer texts, use a sliding window approach
#         embeddings = []
#         for i in range(0, len(tokens), self.stride):
#             chunk = self.tokenizer.convert_tokens_to_string(tokens[i:i + self.max_length])
#             chunk_embedding = self._embed_chunk(chunk)
#             embeddings.append(chunk_embedding)
#
#         # Average the embeddings from all chunks
#         average_embedding = np.mean(embeddings, axis=0)
#         return average_embedding.tolist()
#
#     def _embed_chunk(self, text: str) -> np.ndarray:
#         inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=self.max_length)
#         inputs = {name: tensor.to(self.device) for name, tensor in inputs.items()}
#
#         with torch.no_grad():
#             outputs = self.model(**inputs)
#
#         sentence_embedding = outputs.last_hidden_state[:, 0, :].squeeze().cpu().numpy()
#         return sentence_embedding