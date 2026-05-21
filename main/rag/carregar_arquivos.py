from pypdf import PdfReader
from docx import Document

"""
Lê o documento mediante a extensão dele
"""

def carregar_txt(caminho_arquivo):

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return f.read()


def carregar_pdf(caminho_arquivo):

    texto = ""

    leitor = PdfReader(caminho_arquivo)

    for pagina in leitor.pages:
        texto += pagina.extract_text() + "\n"

    return texto


def carregar_docx(caminho_arquivo):

    doc = Document(caminho_arquivo)

    texto = ""

    for paragrafo in doc.paragraphs:
        texto += paragrafo.text + "\n"

    return texto


def carregar_documento(caminho_arquivo):

    if caminho_arquivo.endswith(".txt"):
        return carregar_txt(caminho_arquivo)

    elif caminho_arquivo.endswith(".pdf"):
        return carregar_pdf(caminho_arquivo)

    elif caminho_arquivo.endswith(".docx"):
        return carregar_docx(caminho_arquivo)

    else:
        raise ValueError("Formato não suportado")