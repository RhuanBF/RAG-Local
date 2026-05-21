from fastapi import APIRouter, UploadFile, File
from main.rag.embeddings import gerar_embeddings
import os
import shutil
from typing import List
from main.rag.carregar_arquivos import carregar_documento
from main.rag.chunker import dividir_em_chunks
from main.rag.salvar_vetores import salvar_chunks

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/upload")#Requisições tipo POST no endereço /upload
async def upload_arquivo(files: List[UploadFile] = File(...)):#Varivael File do JS que guarda os arq
    resultados = []
    
    for file in files:
        caminho_arquivo = os.path.join(UPLOAD_FOLDER, file.filename)
        
        #Guarda na pasta uploads os arquivos recebidos pelo JS
        with open(caminho_arquivo, "wb") as caminho:
            shutil.copyfileobj(file.file, caminho)

        #Le o conteudo do arquivo
        texto = carregar_documento(caminho_arquivo)
        #Faz os chucks conforme o tamanho do texto do arquivo
        chunks = dividir_em_chunks(texto)
        #Gera os vetores
        embeddings = gerar_embeddings(chunks)
        #Salva os chucks no Banco de dados local
        salvar_chunks(chunks, embeddings)
        
        resultados.append({
            "arquivo": file.filename,
            "total_chunks": len(chunks)
        })
        
    return {
        "status": "ok",
        "arquivos_processados": resultados,
        "armazenado_no_chroma": True
    }