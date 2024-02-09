import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return base64.b64encode(ciphertext).decode()

def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext.encode())
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
    return decrypted_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AES encryption and decryption")
    parser.add_argument("-m", "--mode", choices=["encrypt", "decrypt"], required=True, help="Mode: encrypt or decrypt")
    parser.add_argument("-k", "--key", required=True, help="Base64-encoded key")
    parser.add_argument("-d", "--data", required=True, help="Data to encrypt/decrypt")

    args = parser.parse_args()

    key = base64.b64decode(args.key.encode())

    if args.mode == "encrypt":
        encrypted_data = encrypt(args.data, key)
        print("Encrypted Data:", encrypted_data)
    elif args.mode == "decrypt":
        decrypted_data = decrypt(args.data, key)
        print("Decrypted Data:", decrypted_data)
