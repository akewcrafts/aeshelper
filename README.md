# aeshelper

Python3 tools for decrypting and encrypting requests using AES-128bit AES/ECB/PKCS7Padding.

## Usage

### Encryption
To encrypt plaintext data using AES-128bit encryption, use the following command:

```python aes_tool.py -m decrypt -k "your_base64_encoded_key" -d "your_data_to_decrypt"```


Replace `"plaintext"` with the text you want to encrypt.

### Decryption
To decrypt ciphertext data using AES-128bit encryption, use the following command:

```python aes_tool.py -m decrypt -k "your_base64_encoded_key" -d "your_data_to_decrypt"```


Replace `"ciphertext"` with the text you want to decrypt.

## Requirements
- Python 3.x
- pycryptodome library (install using `pip install pycryptodome`)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This tool uses the pycryptodome library for AES encryption and decryption.
