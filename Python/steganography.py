import cv2
import numpy as np


def binary_convert(data):
    """This function converts our data into binary data."""
    if isinstance(data, str):
        return ''.join([format(ord(i), "08b") for i in data])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [format(i, "08b") for i in data]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("This type is unsupported.")


def encode(image_name, secret_data):
    # Reads the image
    image_rows = cv2.imread(image_name)
    # Gives us the maximum no. of bytes to encode.
    n_bytes = image_rows.shape[0] * image_rows.shape[1] * 3 // 8
    print("Maximum bytes to encode are:", n_bytes)
    if len(secret_data) > n_bytes:
        raise ValueError(
            "Insufficient bytes,we will need a bigger image or less data.")
    print("Encoding Data to Image...")
    # This adds a stopping criteria, which is used to guess the
    secret_data += "====="
    data_index = 0
    # Converts the data to binary.
    binary_secret_data = binary_convert(secret_data)
    # Gets the size of the data to hide.
    data_len = len(binary_secret_data)

    for row in image_rows:
        for pixel in row:

            r, g, b = binary_convert(pixel)

            if data_index < data_len:

                pixel[0] = int(r[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:

                pixel[1] = int(g[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:

                pixel[2] = int(b[:-1] + binary_secret_data[data_index], 2)
                data_index += 1

            if data_index >= data_len:
                break
    return image_rows


def decode(image_name):
    print("Decoding data from Image...")
    # Reading the Image
    image_rows = cv2.imread(image_name)
    binary_data = ""
    for row in image_rows:
        for pixel in row:
            r, g, b = binary_convert(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]

    # Splitting the image by 8-bits
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    # Now, we convert the bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "=====":
            break
    return decoded_data[:-5]

# We will assign variables as the name of the input and the output file.
input_img = "img.png" # Enter the name of your image here.
out_img = "img_out.png" # Also, update this accordingly.

# Now we can just call the encode() function to encode the image and save the data to a variable.
enc_image = encode(input_img, "Hi Folks!") # Replace "Hi Folks!" with the data you want to encode.
cv2.imwrite(out_img, enc_image) #Using OpenCV to write the result to an actual image file.

# We can decode the image by simply calling the decode() function.
decode(out_img)
