import chromadb
import uuid

"""
Armazena as informações dentro de um banco de dados (SQL) em uma 
tabela feita pelo chromadb.
"""

#Driver do chromadb no modo pesistente, ele cria uma pasta fisica para armazenar os dados
client = chromadb.PersistentClient(path="banco_de_dados_chroma")

try:
    client.delete_collection("tabela_contexto_rag")#Deleta a tabela documentos quando reinicia
except:
    pass

#Ele cria uma tabela no banco SQL, caso já exista ele abre direto.
collection = client.get_or_create_collection(name="tabela_contexto_rag")

def salvar_chunks(chunks, embeddings):
    ids = []
    for _ in chunks:
        chuck = str(uuid.uuid4())#o chromadb precisa qeu cada elemento tenha um id unico 
        ids.append(chuck)

    #na tabela (collection) é adiciona os parametros
    collection.add(ids=ids,documents=chunks,embeddings=embeddings)
    return len(chunks)#retorna a quantidade de chuks salvos 