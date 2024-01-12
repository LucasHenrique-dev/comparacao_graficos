from pdf_creator import create_pdf


CONTEUDO_PDF = []
titulo_documento = "Comparação Gráficos FLR"
subtitulo_documento = "Comparativo do Simulador C++ com Paper de Emerson"
capitulos = 2

conteudo = """Hello World
Isso é um teste
Quero saber
Quantas linhas
É capaz de escrever
E saber se as linhas irão quebrar
Ou seja
Estou escrevendo
Várias
Linhas
Para
Fins
de
teste
Acho que está bom!
"""

capitulo_1 = {"title": "capitulo1", "image": ["images/gato_laranja.jpg"], "texto": conteudo}
capitulo_2 = {"title": "capitulo2", "image": ["images/gato_laranja.jpg"], "texto": "txt2"}
# capitulo_3 = {"title": "capitulo3", "image": ["im3"], "texto": "txt3"}
# capitulo_4 = {"title": "capitulo4", "image": ["im4"], "texto": "txt4"}

for capitulo_index in range(1, capitulos+1):
    capitulo = vars()[f"capitulo_{capitulo_index}"]
    
    CONTEUDO_PDF.append(capitulo)

# print(CONTEUDO_PDF)

create_pdf("exemplo_formatado.pdf", titulo_documento, subtitulo_documento, CONTEUDO_PDF)
