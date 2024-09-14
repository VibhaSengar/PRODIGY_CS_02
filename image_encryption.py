from PIL import Image

# Encrypt function to manipulate the pixels
def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    pixels = image.load()  # Load pixel data

    # Iterate over each pixel and modify it with the key
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            # Modify each RGB component using a simple mathematical operation
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[i, j] = (r, g, b)  # Set new pixel value

    # Save the encrypted image
    image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

# Decrypt function to reverse the pixel manipulation
def decrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    pixels = image.load()

    # Iterate over each pixel and reverse the modification using the same key
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            # Reverse the modification
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[i, j] = (r, g, b)  # Set original pixel value

    # Save the decrypted image
    image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

# Example usage
if __name__ == "__main__":
    key = 50  # Key used for encryption and decryption

    # File paths for input and output images
    original_image = "C://Users//vibha//Desktop//Prodigy_CS//White Rabbit Images.jpeg"  # Replace with your image path
    encrypted_image = "encrypted_image.png"
    decrypted_image = "decrypted_image.png"

    # Encrypt the image
    encrypt_image(original_image, encrypted_image, key)

    # Decrypt the image
    decrypt_image(encrypted_image, decrypted_image, key)
