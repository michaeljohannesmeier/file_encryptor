
import os
import pathlib
from enum import Enum
import yaml

from loguru import logger
from cryptography.fernet import Fernet




def get_files_to_encrypt(project_root_folder: str):
    with open(os.path.join(project_root_folder, "config.yml")) as stream:
        config = yaml.safe_load(stream)
        return config["file-encryptor"]["files-to-encrypt"]



class Mode(Enum):
    DECRYPT = "decrypt"
    ENCRYPT = "encrypt"

def init_fernet(project_root_folder: str, key = None):
    if not key:
        logger.info("Using key from file: decrypt.key")
        with open(os.path.join(project_root_folder, 'decrypt.key'), 'rb') as filekey:
            key = filekey.read()
    return Fernet(key)

def de_or_encrypt(project_root_folder: str, de_or_encrypt: str, file = None, key = None):
    fernet = init_fernet(project_root_folder, key)
    count = 0
    if file:
        files_to_encrypt = [file]
    else:
        files_to_encrypt = get_files_to_encrypt(project_root_folder)
    for root, _, filenames in os.walk(project_root_folder):
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

def gen_new_key(project_root_folder: str, filename: str = "decrypt.key"):
    key = Fernet.generate_key()
    file_path = os.path.join(project_root_folder, filename)
    with open(file_path, 'wb') as filekey:
      logger.info(f"Saving key to {file_path}")
      filekey.write(key)