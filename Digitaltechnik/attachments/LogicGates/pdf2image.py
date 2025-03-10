import os
import fitz  # PyMuPDF

def convert_pdfs_to_images(directory, zoom=2.0):
    # Iterate through all files in the given directory
    for filename in os.listdir(directory):
        # Check if the file is a PDF
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory, filename)
            # Open the PDF file
            pdf_document = fitz.open(file_path)
            # Iterate through each page
            for page_number in range(pdf_document.page_count):
                page = pdf_document.load_page(page_number)
                # Set the zoom factor (scaling)
                zoom_matrix = fitz.Matrix(zoom, zoom)
                # Render the page to an image with the zoom factor
                pix = page.get_pixmap(matrix=zoom_matrix)
                # Construct the image filename, preserving the original PDF name
                image_filename = f"{os.path.splitext(filename)[0]}_page{page_number + 1}.png"
                image_path = os.path.join(directory, image_filename)
                # Save the image
                pix.save(image_path)
                print(f"Saved {image_path}")

# Set the directory to the current working directory
directory = os.getcwd()

# Call the function to convert PDFs to images with a zoom factor of 2.0 (adjust as needed)
convert_pdfs_to_images(directory, zoom=20.0)