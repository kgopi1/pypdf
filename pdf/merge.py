# To merge list of pdf files . 

# output the files to restult.pdf

from pypdf import PdfWriter

pdfs = ['page-1.pdf', 'page-2.pdf', 'page-3.pdf', 'page-4-5.pdf', 'page-6.pdf']

merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
