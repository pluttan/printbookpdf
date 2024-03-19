from PyPDF2 import PdfFileReader, PdfFileWriter
from sys import argv
import os
import os.path
import pathlib

pdf = PdfFileReader(argv[1])
pdf_writer = PdfFileWriter()
npdf = PdfFileWriter()
for i in range(pdf.getNumPages()):
    npdf.addPage(pdf.getPage(i))
if npdf.getNumPages() % 4 != 0:
    for i in range(4 - npdf.getNumPages() % 4):
        npdf.addBlankPage(612, 792)
for page in range(1, npdf.getNumPages()//2 + 1):
    page2 = npdf.getPage(page - 1)
    page1 = npdf.getPage(npdf.getNumPages() - page)
    pdf_writer.addPage(page1)
    pdf_writer.addPage(page2)

pdf_writer2 = PdfFileWriter()

for i in range(npdf.getNumPages()):
    pdf_writer2.addPage(pdf_writer.getPage(i)
                        if (i % 4 == 0) or (i % 4 == 1) else
                        pdf_writer.getPage(i).rotateCounterClockwise(180)
                        )
# path joining version for other paths
DIR = '/Users/pluttan/Desktop/проекты/printbookpdf/books/'
outputFilename = DIR + pathlib.Path(argv[1]).stem + ".pdf"
with open(outputFilename, "wb") as out:
    pdf_writer2.write(out)


# pdf_writer.addPage(page1
#                        if (page) % 2 == 0 else
#                        page1.rotateCounterClockwise(180)
#                        )
