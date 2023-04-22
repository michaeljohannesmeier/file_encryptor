# File-encryptor

Encrypts or decrypts all files in the parent directory of this package which are listed in: `files_to_encrypt.txt`.

## How to use

- generate a file called `files_to_encrypt.txt` - see `example_files_to_encrypt.txt`
- run `poetry install`
- generate a key for encryption with `poetry run file-encryptor generate-new-key`
- encrypt all files in parent folder of root folder of this project: `poetry run file-encryptor encrypt`
- decrypt all files in parent folder of root folder of this project: `poetry run file-encryptor decrypt`
