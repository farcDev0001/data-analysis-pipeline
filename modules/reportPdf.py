from fpdf import FPDF

class PDF(FPDF):
    """
    Clase hija que hereda de FPDF que define la estructura de un informe para el proyecto actual de análisis de datos
    """
    def header(self,title = 'REPORT'):
        """
        Método que define la cabecera del informe
        args:
            title: String con el título del informe
        """
        
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, title, 1, 0, 'C')
        # Line break
        self.ln(20)
    
    def chapter_body(self,image,text):
        """
        Método que define el cuerpo del informe
        args:
            image: String con la ruta de la imagen
            text: String con la ruta del txt con el texto
        """
        
        self.image(image, 25, 25, 150)
        
        for ele in range(12):
            self.ln()
        # Times 12
        self.set_font('Times', '', 12)
        #Leer
        with open(text, 'rb') as fh:
            txt = fh.read().decode('utf8')
        # Emitir texto justificado
        self.multi_cell(0, 5, txt)
        

    # Page footer
    def footer(self):
        """
        Método que define el pie del informe
        """
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


    def print_chapter(self,image,text):
        """
        Método que integra la imagen y el texto en el cuerpo
        args:
            image: String con la ruta de la imagen
            text: String con la ruta del txt con el texto
        """
        self.chapter_body(image,text)

def exportRep(pathPDF,pathPng,pathTxt = './../inputs/report.txt'):
    """
    Función que inicializa un objeto PDF a partir de las rutas de un mapa de bits y de un txt y lo guarda en forma de pdf 
    en la ruta que se espicifique. 
    args:
        pathPDF: String con la ruta en la que se quiere guardar el pdf
        pathPng: String con la ruta del mapa de bits que se queire integrar en el pdf
        pathTxt. String con la ruta del archivo txt en el que esté el texto que se quiere integrar en el informe
    """
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    pdf.print_chapter(pathPng,pathTxt)
    pdf.output(pathPDF, 'F')

