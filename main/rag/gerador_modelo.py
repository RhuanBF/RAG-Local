import requests

"""
O gerar_resposta recebe a pergunta e os contextos (melhores embedding dos arquivos do usuário).
As informações do prompt e modelo são passadas atraves de um POST (library requests)
para o ollama.
O Ollama utiliza o modelo para responder e retorna a resposta HTTP.
O resultado é formatado em json para pegar uma chave que contém uma key chamada 'response', onde 
estará a resposta do modelo.
"""

OLLAMA_URL = "http://localhost:11434/api/generate" 
MODELO = "qwen2.5:7b" #Modelo utilizado para responder

def gerar_resposta(pergunta,contextos):

    contexto_formatado = "\n\n".join(contextos)

    prompt = f"""
    Você é um Assistente especialista em análise de documentos que fornece respostas extremamente detalhadas, completas e ricas em contexto.

    Sua tarefa é responder à PERGUNTA do usuário baseando-se estritamente no CONTEXTO fornecido abaixo.

    Siga estas diretrizes para a resposta:
    1. Estrutura e detalhe: Não resuma excessivamente. Explique os conceitos por tras da resposta, cite dados, métricas, nomes ou regras explícitas que aparecem no texto. Caso apropriado, use tópicos (bullet points) para organizar as informações.
    2. Fidelidade ao contexto: Se baseie apenas nas informações fornecidas. Não invente fatos, não pressuponha nada fora do texto e não use conhecimentos externos.
    3. Tratemento de ausência: Se o CONTEXTO não contiver informações suficientes para responder a pergunta de forma completa, diga explicitamente: "Não encontrei informações suficientes nos documentos para responder a isso."

    CONTEXTO:
    {contexto_formatado}

    PERGUNTA:
    {pergunta}

    Resposta detalhada:
    """

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    resultado = response.json() #

    return resultado["response"]