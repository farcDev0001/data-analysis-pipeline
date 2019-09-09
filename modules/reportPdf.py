from fpdf import FPDF

class PDF(FPDF):
    def header(self,title = 'REPORT'):
        # Logo
        
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, title, 1, 0, 'C')
        # Line break
        self.ln(20)
    
    def chapter_body(self,image,text):
        
        self.image(image, 25, 25, 150)
        
        for ele in range(12):
            self.ln()
        # Times 12
        self.set_font('Times', '', 12)
        #Leer
        with open(text, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Emitir texto justificado
        self.multi_cell(0, 5, txt)
        

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


    def print_chapter(self,image,text):
        self.chapter_body(image,text)

def exportRep(pathPDF,pathPng,pathTxt = './../inputs/report.txt'):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    pdf.print_chapter(pathPng,pathTxt)
    pdf.output(pathPDF, 'F')

