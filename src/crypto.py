
import os
from enum import Enum
from loguru import logger
from cryptography.fernet import Fernet

with open(os.path.join('.', "files_to_encrypt.txt")) as file:
    FILES_TO_ENCRYPT = [line.rstrip() for line in file]


class Mode(Enum):
    DECRYPT = "decrypt"
    ENCRYPT = "encrypt"

def init_fernet(key = None):
    if not key:
        logger.info("Using key from file: decrypt.key")
        with open(os.path.join('decrypt.key'), 'rb') as filekey:
            key = filekey.read()
    return Fernet(key)

def de_or_encrypt(de_or_encrypt: str, file = None, key = None):
    fernet = init_fernet(key)
    count = 0
    if file:
        files_to_encrypt = [file]
    else:
        files_to_encrypt = FILES_TO_ENCRYPT
    for root, _, filenames in os.walk(os.path.join('.')):
        for filename in filenames:
            for file_to_encrypt in files_to_encrypt:
                filepath = os.path.join(root, filename)
                if not filename == file_to_encrypt or ".git" in filepath:
                    continue
                with open(filepath, 'rb') as file:
                    original = file.read()
                if de_or_encrypt == Mode.DECRYPT.value:
                    logger.info(f"Decrypting: {filepath}")
                    de_or_encrypted = fernet.decrypt(original)
                    count+=1
                elif de_or_encrypt == Mode.ENCRYPT.value:
                    logger.info(f"Encrypting: {filepath}")
                    de_or_encrypted = fernet.encrypt(original)
                    count+=1
                with open(filepath, 'wb') as encrypted_file:
                    encrypted_file.write(de_or_encrypted)
    logger.info(f"Successfully {de_or_encrypt}ed: {count} files")   

def gen_new_key(filepath: str):
    key = Fernet.generate_key()
    with open(filepath, 'wb') as filekey:
      filekey.write(key)