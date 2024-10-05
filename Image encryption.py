# Importing necessary libraries
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Class to handle the GUI and encryption/decryption logic
class ImageEncryptorDecryptor:
    def __init__(self, master):
        self.master = master
        master.title("Image Encryptor/Decryptor")

        # Label for the title
        self.label = Label(master, text="AES Image Encryptor/Decryptor")
        self.label.pack()

        # Button to encrypt image
        self.encrypt_button = Button(master, text="Encrypt Image", command=self.encrypt_image)
        self.encrypt_button.pack()

        # Button to decrypt image
        self.decrypt_button = Button(master, text="Decrypt Image", command=self.decrypt_image)
        self.decrypt_button.pack()

        # Label and entry for the encryption key
        self.key_label = Label(master, text="Enter Key (16, 24, or 32 bytes):")
        self.key_label.pack()
        self.key_entry = Entry(master, show="*")
        self.key_entry.pack()

    def encrypt_image(self):
        key = self.key_entry.get().encode()  # Get the key from the entry field
        if len(key) not in [16, 24, 32]:
            messagebox.showerror("Error", "Key must be 16, 24, or 32 bytes long")
            return

        file_path = filedialog.askopenfilename()  # Open file dialog to select an image
        if not file_path:
            return

        try:
            image = Image.open(file_path)  # Open the image
            image_bytes = image.tobytes()  # Convert image to bytes

            cipher = AES.new(key, AES.MODE_CBC)  # Create a new AES cipher object
            encrypted_bytes = cipher.encrypt(pad(image_bytes, AES.block_size))  # Encrypt the image bytes

            encrypted_image_path = os.path.join(os.path.dirname(file_path), 'encrypted_image.png')
            with open(encrypted_image_path, 'wb') as f:
                f.write(cipher.iv)  # Write the initialization vector (IV)
                f.write(encrypted_bytes)  # Write the encrypted bytes

            messagebox.showinfo("Success", f"Image encrypted and saved to {encrypted_image_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def decrypt_image(self):
        key = self.key_entry.get().encode()  # Get the key from the entry field
        if len(key) not in [16, 24, 32]:
            messagebox.showerror("Error", "Key must be 16, 24, or 32 bytes long")
            return

        file_path = filedialog.askopenfilename()  # Open file dialog to select an encrypted image
        if not file_path:
            return

        try:
            with open(file_path, 'rb') as f:
                iv = f.read(16)  # Read the initialization vector (IV)
                encrypted_bytes = f.read()  # Read the encrypted bytes

            cipher = AES.new(key, AES.MODE_CBC, iv)  # Create a new AES cipher object with the IV
            decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)  # Decrypt and unpad the bytes

            image = Image.frombytes('RGB', (256, 256), decrypted_bytes)  # Create an image from the decrypted bytes
            decrypted_image_path = os.path.join(os.path.dirname(file_path), 'decrypted_image.png')
            image.save(decrypted_image_path)  # Save the decrypted image

            messagebox.showinfo("Success", f"Image decrypted and saved to {decrypted_image_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Run the application
if __name__ == "__main__":
    root = Tk()
    image_encryptor_decryptor = ImageEncryptorDecryptor(root)
    root.mainloop()
