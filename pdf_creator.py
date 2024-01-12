from fpdf import FPDF
from fpdf.enums import XPos, YPos


class PDF(FPDF):
    def __init__(self, title, subtitle):
        super().__init__()
        self.title = title
        self.subtitle = subtitle
        self.header_shown = False  # Flag para controlar se o cabeçalho já foi mostrado

    def header(self):
        if not self.header_shown:
            self.set_font('Helvetica', 'B', 16)
            self.cell(0, 10, self.title, 0, align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_font('Helvetica', 'I', 12)
            self.cell(0, 10, self.subtitle, 0, align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.header_shown = True

    def chapter_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.cell(0, 10, title, 0, align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Helvetica', '', 12)
        self.multi_cell(0, 10, body)
        self.ln(2)
    
    def chapter_image(self, path, posX=None, posY=None, width=0, height=0):
        self.image(path, x=posX, y=posY, w=width, h=height)
    

def create_pdf(file_name, title, subtitle, chapters_info):
    img_w, img_h = 95, 80
    pdf = PDF(title, subtitle)
    pdf.add_page()

    for chapter_info in chapters_info:
        pdf.chapter_title(chapter_info["title"])

        posX, posY = pdf.get_x(), pdf.get_y()
        for index, image in enumerate(chapter_info["image"]):
            if index != 0:
                posX, posY = pdf.get_x() + img_w + 5, pdf.get_y()
            pdf.chapter_image(image, posX, posY, img_w, img_h)
        
        if chapter_info["image"]:
            pdf.set_y(pdf.get_y() + img_h + 5)
        if chapter_info["texto"]:
            pdf.chapter_body(chapter_info["texto"])

    # Salve o PDF em um arquivo
    pdf.output(file_name)


if __name__ == "__main__":
    # Exemplo de uso
    title_example = "Título Épico de Documento"
    subtitle_example = "Subtítulo show de bola"
    content_example = """
        Este é um exemplo de conteúdo para o PDF.
        Pode incluir várias linhas de texto formatado.
        - Listas
        - Outros elementos
        etc.
    """

    chapters_info = [
        {"title": "Capítulo1", "image": ["images/gato_laranja.jpg", "images/gato_cacador.jpg"], "texto": ""},
        {"title": "Capítulo2", "image": [], "texto": content_example}
    ]

    create_pdf("saida/exemplo_formatado.pdf", title_example, subtitle_example, chapters_info)

# if ln != "DEPRECATED":
#             # For backwards compatibility, if "ln" is used we overwrite "new_[xy]".
#             if ln == 0:
#                 new_x = XPos.RIGHT
#                 new_y = YPos.TOP
#             elif ln == 1:
#                 new_x = XPos.LMARGIN
#                 new_y = YPos.NEXT
#             elif ln == 2:
#                 new_x = XPos.LEFT
#                 new_y = YPos.NEXT
