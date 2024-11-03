from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(image_path, shift_value):
    # Open image
    img = Image.open(image_path)
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Encrypt the image by adding shift_value to each pixel
    encrypted_array = (img_array + shift_value) % 256
    
    # Create and save the encrypted image
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    encrypted_image.save('encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'")

# Function to decrypt the image
def decrypt_image(image_path, shift_value):
    # Open the encrypted image
    img = Image.open(image_path)
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Decrypt the image by subtracting shift_value from each pixel
    decrypted_array = (img_array - shift_value) % 256
    
    # Create and save the decrypted image
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))
    decrypted_image.save('decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png'")

# Main function to run the tool
def main():
    choice = input("Do you want to encrypt or decrypt the image? (e/d): ").lower()

    # Get the image path and shift value from the user
    image_path = input("Enter the image path: ")
    shift_value = int(input("Enter the shift value (a number between 1 and 255): "))

    if choice == 'e':
        encrypt_image(image_path, shift_value)
    elif choice == 'd':
        decrypt_image(image_path, shift_value)
    else:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()
