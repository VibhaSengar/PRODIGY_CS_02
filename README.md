# PRODIGY_CS_02
This task involves developing a simple image encryption tool using pixel manipulation. The code applies basic mathematical operations to encrypt and decrypt an image by adjusting the RGB values of each pixel. Users can encrypt an image with a key and decrypt it using the same key to restore the original image.
1. Image Processing with Pillow (PIL)
The Pillow library (PIL) is used to manipulate images in Python. The following steps are applied to achieve the encryption and decryption:

Image.open(input_image_path): This function opens the image specified by the file path, enabling further manipulation.
pixels = image.load(): This function loads the pixel data of the image into a variable, allowing access to each individual pixel for modification.
2. Encrypting the Image (encrypt_image)
The encrypt_image function manipulates the pixel values (RGB) of the image by adding a user-defined key to each component of the pixel:

RGB Values: Each pixel in an image is composed of three values representing the Red, Green, and Blue (RGB) color components.
The encryption process modifies each of these values by adding the key and taking the result modulo 256 to ensure the value stays within the range of 0-255 (the valid range for RGB values).
Encryption Formula: For each pixel (r, g, b):

r = (r + key) % 256
g = (g + key) % 256
b = (b + key) % 256
3. Decrypting the Image (decrypt_image)
The decrypt_image function reverses the pixel manipulation by subtracting the key from each RGB component, effectively restoring the original pixel values:

For each pixel (r, g, b), the function reverses the operation performed during encryption.
Decryption Formula: For each pixel (r, g, b):

r = (r - key) % 256
g = (g - key) % 256
b = (b - key) % 256
4. Key Used for Encryption/Decryption
The key used in both encryption and decryption is an integer that defines how much each pixel value is shifted. The same key must be used to both encrypt and decrypt the image:

If a different key is used for decryption, the image will not be restored to its original form.
5. Main Function and Usage
In the main section of the code:

The user is asked to provide the input image path (the image to be encrypted), the output paths for the encrypted image and decrypted image, and the key for encryption.
The image is first encrypted and saved as encrypted_image.png, then decrypted using the same key and saved as decrypted_image.png.
