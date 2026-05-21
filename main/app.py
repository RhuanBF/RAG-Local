from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from main.routes.upload import router as upload_router
from main.routes.chat import router as chat_router

#Instância do motor FastAPI
app = FastAPI(title="RAG Local API")

# Permissões e portas
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#É criado uma pasta virtual static e o que for pedido dentro dessa pasta
#será lido dentro da pasta static do disco
app.mount("/static", StaticFiles(directory="static"), name="static")

#rotas
app.include_router(upload_router)
app.include_router(chat_router)


#tela principal do endereço padrão
@app.get("/")
async def home():

    return FileResponse("static/index.html")