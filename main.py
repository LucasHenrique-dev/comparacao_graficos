from pdf_creator import create_pdf, generate_new_header, save_pdf


CONTEUDO_PDF = []
documento = "pdf_varias_secoes"

cabecalho_1 = "Estudos 1"
subtitulo_1 = "Início dos Estudos"
capitulos = 2

cabecalho_2 = "Estudos 2"
subtitulo_2 = "Estudos Aprofundados"
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

my_pdf = create_pdf(cabecalho_1, subtitulo_1, CONTEUDO_PDF)

my_pdf = generate_new_header(my_pdf, cabecalho_2, subtitulo_2, CONTEUDO_PDF)

save_pdf(my_pdf, documento)
