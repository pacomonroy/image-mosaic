from PIL import Image, ImageOps

def invert_image(image_path, output_path):
    image = Image.open(image_path).convert("L")  # Convert image to grayscale
    inverted_image = ImageOps.invert(image)  # Invert colors
    inverted_image.save(output_path)

invert_image('input.png', 'output.png')
