# AES Key Generator

A simple Python script to generate a random AES key of a given length.

## Opportunities

* Generate a key of **8**, **16**, **32** or **64** bytes.
* Output the key to the console in hexadecimal format.
* Saving the key to a file (if necessary).

## Requirements

* Python **3.6** or higher.
* Modules from the standard library: `argparse`, `secrets`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/IVSamDev/AES-Key-Generator.git
   cd aes-key-generator
   ```
2. Make sure you have Python 3.6+ installed:

   ````bash
   python3 --version
   ````

## Usage

Run the script from the console, specifying the key length and (optionally) the file to save:

```bash
python3 key.py --size <bytes> [--output <file>]
```

### Attributes (parameters)

| Option           | Description                                    | Commitment      | Possible values       |
| ---------------- | ---------------------------------------------- | --------------- | --------------------- |
| `-s`, `--size`   | Key length in bytes                            | **necessarily** | `8`, `16`, `32`, `64` |
| `-o`, `--output` | File path to save the key (hex string)         | optionally      | `<file_name>.txt`     |

### Examples

1. Generate a 16-byte key and output to the console:

   ```bash
   python3 key.py -s 16
   ```

2. Generate a 32-byte key and save to the `key.txt` file:

   ````bash
   python3 key.py --size 32 --output key.txt
   ````

## License

MIT License © IVSamDev
