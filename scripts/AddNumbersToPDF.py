####### Page Numbering Script #########
# Automatically adds page numbers to 
# each page of an existing PDF document.
#######################################


from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import os

input_pdf = "input.pdf"
output_pdf = "numbered.pdf"

reader = PdfReader(input_pdf)
writer = PdfWriter()

for i, page in enumerate(reader.pages):
    # Get page size
    width = float(page.mediabox.width)
    height = float(page.mediabox.height)

    # Create overlay PDF
    temp_pdf = "temp.pdf"
    c = canvas.Canvas(temp_pdf, pagesize=(width, height))

    page_number_text = str(i + 1)

    # Draw centered at bottom (y=20 points)
    c.drawCentredString(width / 2, 20, page_number_text)

    c.save()

    # Merge overlay
    overlay = PdfReader(temp_pdf).pages[0]
    page.merge_page(overlay)
    writer.add_page(page)

# Write output
with open(output_pdf, "wb") as f:
    writer.write(f)

# Cleanup
os.remove("temp.pdf")