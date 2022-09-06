## pip install fpdf==1.7

## Import
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

## Adding meta data to the PDF file
pdf.set_title("Test PDF")
pdf.set_author("Giridhar")
pdf.set_creator("Honeybadger")
pdf.set_subject("Test PDF created using PypDF2")
pdf.set_keywords("PDF, Python, Tutorial")

pdf.add_page()

## Add text
pdf.set_font("Arial", size=18)
pdf.set_text_color(0, 0, 255)
pdf.cell(200, 10, txt="Hello World!", ln=1, align="C")

pdf.set_font("Arial", size=12)
pdf.set_text_color(0, 0, 0)
pdf.cell(200, 10, txt="This pdf is created using FPDF in Python.", ln=2, align="C")

## Add image
#pdf.image(name="boy_night.jpg", h=107, type="JPG")

## Save the PDF file
pdf.output("test_pdf.pdf")
print("pdf has been created successfully....")