from pdf2image import convert_from_path

def pdf_to_jpeg(pdf_path, output_folder):
    # Convert the PDF to a list of PIL Image objects
    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        # Save each image as a JPEG file
        image.save(f"{output_folder}/page_{i + 1}.jpg", "JPEG")

# Replace these with your PDF file path and output folder
pdf_file = "floor_plans/floor2.pdf.pdf"
output_folder = "floor_plans"

pdf_to_jpeg(pdf_file, output_folder)