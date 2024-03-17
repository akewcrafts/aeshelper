# AES128 ECB/PKCS7Padding Encryption and Decryption 

![AES Logo](https://blog.cactusjack.top/upload/2021/10/1_RshQA9waAi-S7vdZkOKN6A-762c9a8f2ef6499b9457bfdf62a62b7e.jpeg)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This Python script provides functionality for AES-128bit (AES/ECB/PKCS7Padding) encryption and decryption using the `Crypto.Cipher` module.

## Requirements

- Python 3.x
- `Crypto.Cipher` module (provided by `pycryptodome`)
- `Crypto.Util.Padding` module (provided by `pycryptodome`)
- `base64` module (standard library)

## Installation

1. Make sure you have Python 3.x installed on your system. If not, download and install it from the [official Python website](https://www.python.org/downloads/).

2. Install the required libraries using pip:

   ```bash
   pip install pycryptodome

## Usage

To use the script, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/aes-encryption-decryption.git

3. Navigate to the project directory:

    ```bash

    cd aes-encryption-decryption

4. Run the script with the following command:

    ```bash
    python aes_script.py -m [encrypt/decrypt] -k [base64-encoded-key] -d [data-to-encrypt/decrypt]
    ```
    - *Replace [encrypt/decrypt] with either encrypt or decrypt based on your operation.*
    - *Replace [base64-encoded-key] with your base64-encoded encryption key.*
    - *Replace [data-to-encrypt/decrypt] with the data you want to encrypt or decrypt.*
    - *Use python3 command if you have multiple python version on your PATH*
      
# Script Explanation

The script provides two main functions:
  
`encrypt(plaintext, key)`: Encrypts the given plaintext using AES encryption and a base64-encoded key.

`decrypt(ciphertext, key)`: Decrypts the given ciphertext using AES decryption and a base64-encoded key.

# Examples

**Encrypting data:**

  ```bash
  python aes_script.py -m encrypt -k YWRtaW4= -d "Hello, World!"
  ```
**Decrypting data:**

```bash
python aes_script.py -m decrypt -k YWRtaW4= -d "U2FsdGVkX19ImoBfAXJdD8uvU3q5rMfiGgoyKzktH/E="
```

# License

This project is licensed under the MIT License.
