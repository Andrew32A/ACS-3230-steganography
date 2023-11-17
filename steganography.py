"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    - Lesson Plan: https://tech-at-du.github.io/ACS-3230-Web-Security/#/Lessons/Steganography

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""
# TODO: Run `pip3 install Pillow` before running the code.
from PIL import Image, ImageDraw, ImageFont


def decode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    for x in range(x_size):
        for y in range(y_size):
            red_pixel = red_channel.getpixel((x, y))
            lsb = red_pixel % 2
            if lsb == 1:
                pixels[x, y] = (255, 255, 255)
            else:
                pixels[x, y] = (0, 0, 0)

    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
    print(red_channel)  # Start coding here!

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")

def encode_image(path_to_original_png, path_to_text_png):
    """
    TODO: Add docstring and complete implementation.
    """
    original_image = Image.open(path_to_original_png)
    text_image = Image.open(path_to_text_png)
    encoded_image = Image.new("RGB", original_image.size)

    for y in range(original_image.size[1]):
        for x in range(original_image.size[0]):
            original_pixel = original_image.getpixel((x, y))
            text_pixel = text_image.getpixel((x, y))
            new_red_pixel = (original_pixel[0] & ~1) | (text_pixel[0] & 1)
            new_green_pixel = (original_pixel[1] & ~1) | (text_pixel[1] & 1)
            new_blue_pixel = (original_pixel[2] & ~1) | (text_pixel[2] & 1)

            encoded_image.putpixel((x, y), (new_red_pixel, new_green_pixel, new_blue_pixel))

    encoded_image.save("encoded_image.png")

def write_text(text_to_write, path_to_output_png):
    """
    TODO: Add docstring and complete implementation.
    """
    black_background = Image.new("RGB", (1600, 900), "black")
    draw = ImageDraw.Draw(black_background)
    font = ImageFont.load_default()

    position = (200, 200)
    color = "white" 

    draw.text(position, text_to_write, fill=color, font=font)
    black_background.save(path_to_output_png)

secret_text = """
"Sometimes life is like this dark tunnel 
you can't always see the light at the end 
of the tunnel but if you just keep moving 
you will come to a better place"
-Uncle Iroh
"""

write_text(secret_text, "secret_text.png")
encode_image("original_image.png", "secret_text.png")
decode_image("encoded_image.png")
