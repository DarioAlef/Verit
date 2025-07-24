# # Hybrid Search para otimizar buscas jurídicas

# class HybridSearch:
#     def __init__(self):
#         self.vector_search = ChromaDb()
#         self.text_search = ElasticSearch()  # Para busca por termos exatos
        
#     def search(self, query: str):
#         # Combina busca vetorial + busca por palavras-chave
#         vector_results = self.vector_search.query(query)
#         text_results = self.text_search.query(query)
#         return self.merge_results(vector_results, text_results)