# File-encryptor

Encrypts or decrypts all files specified in: `config.yml`.

## How to use

- place this package into the root folder of your package where you want to use it and install it via poetry
- generate a file called `config.yml` - see `example_config.yml`
- specify base path and files which should be encrypted
- run `poetry install`
- generate a key for encryption with `poetry run file-encryptor generate-new-key`
- encrypt all files in parent folder of root folder of this project: `poetry run file-encryptor encrypt`
- decrypt all files in parent folder of root folder of this project: `poetry run file-encryptor decrypt`
