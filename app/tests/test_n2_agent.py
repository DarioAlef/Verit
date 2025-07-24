from agno.playground import Playground, serve_playground_app

from agno.agent import Agent
from agno.models.groq import Groq
from agno.vectordb.chroma import ChromaDb
from agno.storage.sqlite import SqliteStorage
from agno.knowledge.url import UrlKnowledge
from app.utils.config import settings
from agno.embedder.base import Embedder
from fastembed import TextEmbedding
from app.tools.fastembed_wrapper import Fastembed_wrapper

# tamanho do embedder
embed_small = Fastembed_wrapper("BAAI/bge-small-en-v1.5")    # ~384 dimensões
# embed_base = Fastembed_wrapper("BAAI/bge-base-en-v1.5")      # ~768 dimensões  
# embed_large = Fastembed_wrapper("BAAI/bge-large-en-v1.5")    # ~1024 dimensões
# embed_mini = Fastembed_wrapper("sentence-transformers/all-MiniLM-L6-v2")  # ~384 dimensões

# base de conhecimento do Agente
knowledge = UrlKnowledge(
    urls=[
        # URLs de artigos específicos (menores)
        'https://www.jusbrasil.com.br/artigos/principio-da-legalidade',
        'https://www.todamateria.com.br/principio-da-legalidade'
    ],
    vector_db=ChromaDb(
        path='temp/lexi_knowledge',
        collection='legal_docs',
        embedder=embed_small
    ),
)

agent = Agent(
    name='Lexi',
    model=Groq(id='deepseek-r1-distill-llama-70b', api_key=settings.groq_api_key),
    instructions=[
        'Você é a Verit, assistente jurídico especializado em Direito Brasileiro.',
        'Pesquise sempre na base de conhecimento antes de responder.',
        'Cite os artigos e leis relevantes quando disponíveis.',
        'Mantenha linguagem clara e didática para estudantes de concursos.',
    ],
    knowledge=knowledge,
    storage=SqliteStorage(table_name='lexi_sessions', db_file='temp/lexi.db'),
    markdown=True,
)


if __name__ == '__main__':
    print(embed_small.get_model_info())
    agent.knowledge.load(recreate=False)
    agent.print_response("O que é o princípio da legalidade?", stream=True)



# app = Playground(
#     agents=[agent]).get_app()

# if __name__ == '__main__':
#     serve_playground_app('stocks:app', reload=True)