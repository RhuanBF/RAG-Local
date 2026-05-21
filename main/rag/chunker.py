def dividir_em_chunks(texto,tamanho_chunk=500,sobreposicao=50):

    """
    dividir_em_chucks irá pegar o texto bruto dos arquivos e transformar 
    em chucks de 500 caracteres com uma margem de 50 palavras em cada chucks,
    isso é feito para caso o chuck quebre um contexto, haverá 50 palavras no 
    fim do primeiro e no inicio do segundo chuck (evitando quebrar contexto).
    """

    chunks = []
    inicio = 0

    while inicio < len(texto):
        fim = inicio + tamanho_chunk #Calcula: inicio(0) + chuck atual(500)
        chunk = texto[inicio:fim]#Pega as palavras 0 ao 500 e guarda na lista
        chunks.append(chunk)#pega o chuck e manda para a lista chucks
        inicio += tamanho_chunk - sobreposicao # adiciona no inicio (500 - 50 = 450)
    return chunks