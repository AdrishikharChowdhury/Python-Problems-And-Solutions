import fitz  # PyMuPDF
from docx import Document

pdf_file = r"C:\Users\amiad\Downloads\Objective Questions for CA4.pdf"
docx_file = r"C:\Users\amiad\Downloads\Objective Questions for CA4.docx"

# Open the PDF
pdf = fitz.open(pdf_file)
doc = Document()

# Extract text from each page
for page_num in range(len(pdf)):
    page = pdf[page_num]
    text = page.get_text()
    doc.add_paragraph(text)

# Save to DOCX
doc.save(docx_file)
print("PDF converted to DOCX successfully using PyMuPDF!")
