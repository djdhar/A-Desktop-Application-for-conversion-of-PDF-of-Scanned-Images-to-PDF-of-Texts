from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from PyPDF2 import PdfFileMerger
import os

def GeneratePdf(pages,pdfname):
    i=0
    pdfs=[]
    for page in pages:
        i+=1
        details = page[0]
        height = page[1]
        width = page[2]
        c = canvas.Canvas("page"+str(i)+".pdf", pagesize = (width, height))
        pdfs.append("page"+str(i)+".pdf")
        for info in details:
            string = info[0]
            x = info[1][0]
            y = info[1][1]
            w = info[1][2]
            h = info[1][3] 
            c.setFont("Times-Roman", 20)
            c.setFillColorRGB(255,0,0)
            #c.drawCentredString(150, 2.5*inch, "Student details")
            c.drawString(x,height-y, string)
            #c.drawString()
        c.showPage()
        c.save()
    
    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)
        os.system("rm "+pdf)

    merger.write(pdfname[:-4]+"_ocr.pdf")
    merger.close()
    return pdfname[:-4]+"_ocr.pdf"
