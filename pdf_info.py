# https://www.honeybadger.io/blog/python-pdf/
# pip install pypdf2 fpdf2
# pip install pycryptodome

## Import
from PyPDF2 import PdfFileReader

## Setup
pdf = PdfFileReader(open('x:\\xxx.pdf', "rb"))
info = pdf.getDocumentInfo()
number_of_pages = pdf.getNumPages()

pdf_info = f"""
    Information about {info.title}:
    Author: {info.author}
    Creator: {info.creator}
    Producer: {info.producer}
    Subject: {info.subject}
    Title: {info.title}
    Number of pages: {number_of_pages}
  """

print(pdf_info)
