"""FILE-ENCRYPTOR CLI main."""

import sys

import click
from loguru import logger

from .crypto import de_or_encrypt, gen_new_key



logger.remove()
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>", level="INFO")

@click.group()
def file_encryptor():
    """FILE-ENCRYPTOR CLI HELPER."""
    pass

@click.command()
@click.option("--file", "-f", help="File to decrypt - defaults to all files specified in crypto.py")
@click.option("--key", "-k", help="Fernet key - defaults to value in decrypt.key file")
def decrypt(file, key):
    """Decrypts all files specified in crypto.py"""
    de_or_encrypt("decrypt", file, key)

@click.command()
@click.option("--file", "-f", help="File to encrypt - defaults to all files specified in crypto.py")
@click.option("--key", "-k", help="Fernet key - defaults to value in decrypt.key file")
def encrypt(file, key):
    """Encrypts all files specified in crypto.py"""
    de_or_encrypt("encrypt", file, key)

@click.command()
@click.option("--filepath", "-f", help="Filepath to save new key to", default="decrypt.key")
def generate_new_key(filepath):
    """Encrypts all files specified in crypto.py"""
    gen_new_key(filepath)




file_encryptor.add_command(decrypt)
file_encryptor.add_command(encrypt)
file_encryptor.add_command(generate_new_key)


