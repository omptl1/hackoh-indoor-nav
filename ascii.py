import PIL.Image



def to_grayscale(image):
    return image.convert("L")

# Function to resize the image
def resize_image(image, width, height):
    return image.resize((width, height))

# Function to convert an image to ASCII art
def image_to_ascii(image, scale_factor=1.0):
    ascii_chars = "@%#*+=-:. "
    ascii_str = ""
    
    image = resize_image(image, int(image.width * scale_factor), int(image.height * scale_factor))
    
    for pixel_value in image.getdata():
        ascii_str += ascii_chars[pixel_value // 25]
        if len(ascii_str) == image.width:
            ascii_str += '\n'
    
    return ascii_str

# Main function to convert a PDF image to ASCII art
def pdf_image_to_ascii(pdf_file_path, page_number, scale_factor=0.5):
    try:
        pdf_file = PyPDF2.PdfFileReader(open(pdf_file_path, 'rb'))
        page = pdf_file.getPage(page_number)
        xObject = page['/Resources']['/XObject'].get_object()
        image = xObject.get_object()
        
        if image['/ColorSpace'] is not None:
            if image['/ColorSpace'] == '/DeviceRGB':
                image = to_grayscale(image)
            
            ascii_art = image_to_ascii(image, scale_factor)
            return ascii_art
        else:
            return "Image doesn't have a recognized color space."
    except Exception as e:
        return str(e)

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_image_to_ascii.py <pdf_file_path> <page_number>")
        sys.exit(1)
    
    pdf_file_path = sys.argv[1]
    page_number = int(sys.argv[2])
    
    ascii_art = pdf_image_to_ascii(pdf_file_path, page_number)
    print(ascii_art)