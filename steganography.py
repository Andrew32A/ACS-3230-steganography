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
from PIL import Image


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


def encode_image(path_to_png, message):
    """
    TODO: Add docstring and complete implementation.
    """
    original_image = Image.open(path_to_png)
    red_channel, green_channel, blue_channel = original_image.split()
    
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '11111111'
    binary_message += '0' * (red_channel.size[0] * red_channel.size[1] - len(binary_message))
    
    encoded_image = Image.new("RGB", original_image.size)
    pixels = encoded_image.load()
    
    idx = 0
    for y in range(red_channel.size[1]):
        for x in range(red_channel.size[0]):
            red_pixel = red_channel.getpixel((x, y))
            green_pixel = green_channel.getpixel((x, y))
            blue_pixel = blue_channel.getpixel((x, y))
            
            if idx < len(binary_message):
                new_red_pixel = (red_pixel & ~1) | int(binary_message[idx])
                idx += 1
            else:
                new_red_pixel = red_pixel
            
            pixels[x, y] = (new_red_pixel, green_pixel, blue_pixel)
    
    encoded_image.save("encoded_image.png")

def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass

decode_image('encoded-imgs/encoded_sample.png')
# decode_image('encoded_image.png')

# encode_image('./test-input.jpeg', 'Hello World!')



