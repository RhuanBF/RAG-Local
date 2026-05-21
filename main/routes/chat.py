from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from main.rag.recuperacao_contexto import buscar_contexto
from main.rag.gerador_modelo import gerar_resposta

router = APIRouter()

@router.post("/chat")#Requisições tipo POST no endereço /chat
async def chat(request: Request):

    data = await request.json()#Pega o valor da JS do campo texto do usuário e guardar em data

    pergunta = data.get("mensagem", "")
    usuario_id = data.get("usuario_id", "anonimo")

    print(f"Usuário: {usuario_id}")
    print(f"Mensagem: {pergunta}")

    # busca contexto no banco mediante a pergunta
    contexto = buscar_contexto(pergunta)

    # gera resposta depois de receber o contexto
    resposta = gerar_resposta(
        pergunta=pergunta,
        contextos=contexto
    )

    print(f"Resposta: {resposta}")

    return JSONResponse({
        "resposta": resposta,
        "contextos_usados": contexto
    })