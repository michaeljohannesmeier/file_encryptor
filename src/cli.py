"""FILE-ENCRYPTOR CLI main."""

import sys
import pathlib

import click
from loguru import logger

from .crypto import de_or_encrypt, gen_new_key



logger.remove()
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>", level="INFO")

def get_project_root_path():
    return pathlib.Path(__file__).parent.parent.parent.absolute()

@click.group()
def file_encryptor():
    """FILE-ENCRYPTOR CLI HELPER."""
    pass

@click.command()
@click.option("--file", "-f", help="File to decrypt - defaults to all files specified in crypto.py")
@click.option("--key", "-k", help="Fernet key - defaults to value in decrypt.key file")
@click.option("--path", "-p", help="Path of project folder where files should be decrypted", default=get_project_root_path())
def decrypt(path, file, key):
    """Decrypts all files specified in crypto.py"""
    de_or_encrypt(path, "decrypt", file, key)

@click.command()
@click.option("--file", "-f", help="File to encrypt - defaults to all files specified in crypto.py")
@click.option("--key", "-k", help="Fernet key - defaults to value in decrypt.key file")
@click.option("--path", "-p", help="Path of project folder where files should be decrypted", default=get_project_root_path())
def encrypt(path, file, key):
    """Encrypts all files specified in crypto.py"""
    de_or_encrypt(path, "encrypt", file, key)

@click.command()
@click.option("--path", "-p", help="Folder path to save new key to", default=get_project_root_path())
@click.option("--filename", "-f", help="Filename to save new key to", default="decrypt.key")
def generate_new_key(path, filename):
    """Encrypts all files specified in crypto.py"""
    gen_new_key(path, filename)




file_encryptor.add_command(decrypt)
file_encryptor.add_command(encrypt)
file_encryptor.add_command(generate_new_key)


