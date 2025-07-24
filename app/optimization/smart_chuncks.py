# # Criar chuncks inteligentes para documentos jurídicos
# # Dividir por artigos, seções e tamanho
# # Considerar contexto jurídico e estrutura do documento

from typing import List

class JuridicalTextChunker:
    def __init__(self, chunk_size: int = 1000, overlap: int = 200):
        self.chunk_size = chunk_size
        self.overlap = overlap
        
    def split_by_articles(self, text: str) -> List[str]:
        """Divide por artigos jurídicos (Art. 1º, Art. 2º, etc.)"""
        
    def split_by_sections(self, text: str) -> List[str]:
        """Divide por seções e capítulos"""
        
    def smart_chunk(self, text: str) -> List[str]:
        """Combina divisão por estrutura jurídica + tamanho"""