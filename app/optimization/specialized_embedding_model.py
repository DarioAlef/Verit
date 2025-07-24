# # Especialista em otimização de embeddings para textos jurídicos brasileiros
# # Utiliza Fastembed para embeddings rápidos e eficientes

# from app.tools.fastembed_wrapper import Fastembed_wrapper

# class SpecializedLegalEmbedder(Fastembed_wrapper):
#     def __init__(self):
#         # Usar modelo treinado para textos jurídicos brasileiros
#         super().__init__("legal-bert-portuguese")
        
#     def get_contextual_embedding(self, text: str, context: str):
#         """Embedding considerando contexto jurídico"""