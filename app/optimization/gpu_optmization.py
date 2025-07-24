# # Configurações otimizadas para GPU
# # Utilização eficiente de GPU para embeddings
# # Uso de multi-processamento para acelerar o processo

# import os
# import torch

# class GPUOptimizedEmbedder:
#     def __init__(self):
#         self.device = "cuda" if torch.cuda.is_available() else "cpu"
#         self.batch_size = 128 if self.device == "cuda" else 32
        
# # Uso eficiente de CPU cores
# class MultiProcessEmbedder:
#     def __init__(self, num_workers: int = None):
#         self.num_workers = num_workers or os.cpu_count()