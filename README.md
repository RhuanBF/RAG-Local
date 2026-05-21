# Assistente RAG Local com LLM

Este é um projeto de RAG casual, funcionalidade para ler e compreender arquivos (`.txt`, `.pdf` e `.docx`), compreende texto apenas, com um resultado muito bom e roda de forma 100% local e privada. O sistema permite uploads de vários arquivos, possui o processamento em lote e utiliza a estratégia de **chunking** que consiste em quebrar o texto em fatias menores, armazena o texto em vetores (**embedding**) em um banco de dados e utiliza um LLM (**Modelo de Linguagem**) para poder responder às perguntas com base nos arquivos fornecidos.

### Funcionalidades:
* **Upload em Lote:** Processamento assíncrono para receber vários arquivos simultaneamente.
* **Formatos Textuais:** Suporte muito bem com extensões como `.txt`, `.docx` e `.pdf`.
* **Busca Semântica no contexto:** Utiliza busca por similaridade com a pergunta para recuperar contextos relevantes antes de passar para a LLM, garantindo não ter alucinações e ter respostas precisas.

### Tecnologias usadas:
* **Backend:** FastAPI (Utilizando Python)
* **Banco Vetorial:** ChromaDB (SQL)
* **Gerenciador e Modelo:** Ollama (Modelo Qwen2.5:7b)
* **Processamento de Arquivos:** PyPDF e Docx
* **Frontend:** HTML5, CSS3 e JavaScript

### Como rodar o Projeto:
1. **Baixe o modelo no Ollama:**
   Verifique se possui o Ollama instalado junto ao modelo. Abra o cmd(terminal) e execute o comando.
   
   cmd:
   ollama run qwen2.5:7b

2. **Instale as dependências do Python:**
    No cmd instale.

    cmd:
    pip install fastapi uvicorn chromadb pypdf python-docx

3. **Inicie o servidor do FastAPI:**
    No cmd execute o comando para iniciar a API.

    cmd:
    uvicorn main.app:app --reload

4. **Acesse no navegador:**
    Com o servidor rodando, abra o navegador e acesse o endereço local:
    http://127.0.0.1:8000