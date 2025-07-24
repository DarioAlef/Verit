# # Processamento assíncrono e paralelo para otimização de desempenho


# import asyncio
# from typing import List
# from tools.fastembed_wrapper import Fastembed_wrapper
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# class FastembedWrapperAsync(Fastembed_wrapper):
#     async def process_documents_batch(self, documents: List[str], batch_size: int = 50):
#         """Processa documentos em paralelo"""
#         with ThreadPoolExecutor(max_workers=4) as executor:
#             tasks = []
#             for i in range(0, len(documents), batch_size):
#                 batch = documents[i:i + batch_size]
#                 task = executor.submit(self._process_batch, batch)
#                 tasks.append(task)
            
#             results = await asyncio.gather(*tasks)
#             return results