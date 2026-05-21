from main.rag.embeddings import gerar_embedding
from main.rag.salvar_vetores import collection

"""
Transforma a pergunta em embedding(vetores) e procura a proximidade do contexto
dentro do banco e retorna os resultado(documentos)
"""

def buscar_contexto(pergunta,top_k=5):#top_k é um parametro para pegar os 5 melhores resultados

    # transforma pergunta do usuário em embedding
    embedding_pergunta = gerar_embedding(pergunta)

    #o chromadb faz uma query no banco com o embedding(vetor) da pergunta para comparar com a
    # similaridade dos embedding presente no banco, ele irá para a busca quando encontrar os
    # 5 documentos(top_k) parecidos 
    resultados = collection.query(query_embeddings=[embedding_pergunta],n_results=top_k)

    #Pega a lista de texto sepada pelo o chromadb na chave da lista documentos
    documentos = resultados["documents"][0]

    return documentos