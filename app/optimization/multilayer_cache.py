# # Cache multi-camadas em memória + Redis + Disco


# import redis

# class EmbeddingCache:
#     def __init__(self):
#         self.memory_cache = {}  # Cache rápido
#         self.redis_cache = redis.Redis()  # Cache médio
#         self.disk_cache = {}  # Cache persistente
        
#      def get_embedding(self, text_hash: str):
#         # 1. Tenta memória (mais rápido)
#         # 2. Tenta Redis (médio)
#         # 3. Tenta disco (mais lento)
#         # 4. Calcula se não encontrou