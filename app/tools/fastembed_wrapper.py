from agno.embedder.base import Embedder
from fastembed import TextEmbedding
from typing import Optional

# empacotador da classe Embedder do agno, para que o Agno
# possa usar o fastembed como um embedder
class Fastembed_wrapper(Embedder): 
    def __init__(self, model_name: Optional[str] = None):
        super().__init__()
        
        
        # Inicializa o modelo baseado no parâmetro
        if model_name is None:
            self.embedding_model = TextEmbedding() # modelo padrão
            self.model_name = "fastembed-default"
        else:
            self.embedding_model = TextEmbedding(model_name)
            self.model_name = model_name

        self._discover_dimensions()  
        
    # teste para verificar as dimensões do modelo carregado
    def _discover_dimensions(self):
        try:
            test_embedding = list(self.embedding_model.embed(['text_test']))
            self.dimensions = len(test_embedding[0])
            print(f'Modelo {self.model_name} tem {self.dimensions} dimensões.')
        except Exception as e:
            print(f'Erro ao descobrir dimensões do modelo {self.model_name}: {e}')
            self.dimensions = None


    # método para obter o embedding e o uso de tokens
    def get_embedding_and_usage(self, text: str):
        make_embeddings = list(self.embedding_model.embed([text]))
        get_embedding = make_embeddings[0].tolist()
        usage = {"tokens": len(text.split())}
        return get_embedding, usage
    
    
    
    def get_model_info(self):
        return {
            "model_name": self.model_name,
            "dimensions": self.dimensions
        }