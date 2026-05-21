from sentence_transformers import SentenceTransformer

"""
Transforma os textos em vetores que serão organizados em 
um espaço multidimensional para a IA pegar o contexto e o
significado.

gerar_embedding texto unico
gerar_embeddings um conjunto de textos

"""

# modelo global do transformers
modelo_embedding = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2" #Esse modelo acho que tem 460m
)

def gerar_embedding(texto):

    embedding = modelo_embedding.encode(texto)

    return embedding.tolist()


def gerar_embeddings(lista_textos):

    embeddings = modelo_embedding.encode(lista_textos)

    return embeddings.tolist()