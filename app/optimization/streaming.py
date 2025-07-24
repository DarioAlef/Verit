# otimização e streaming

from typing import List


class StreamingProcessor:
    def process_pdf_stream(self, pdf_path: str):
        """Processa PDF página por página, não carrega tudo na memória"""
        for page_num, page_text in self.extract_pages_streaming(pdf_path):
            yield self.process_page(page_text)
            
    def incremental_vectorization(self, new_documents: List[str]):
        """Adiciona novos documentos sem reprocessar tudo"""