import argparse
import secrets


def generate_aes_key(length: int) -> bytes:
    if length not in (8, 16, 32, 64):
        raise ValueError("Allowable key lengths: 8, 16, 32 or 64 bytes")
    return secrets.token_bytes(length)

def main():
    parser = argparse.ArgumentParser(
        description="Generate AES key of specified length in bytes"
    )
    parser.add_argument(
        "-s", "--size",
        type=int,
        choices=[8, 16, 32, 64],
        required=True,
        help="Key length in bytes: 8, 16, 32 or 64"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="File for saving the key (optional)"
    )

    args = parser.parse_args()
    key = generate_aes_key(args.size)

    # Key output in hexadecimal form
    hex_key = key.hex()
    print(f"Generated AES key ({args.size} byte): {hex_key}")

    # Saving to file, if specified
    if args.output:
        with open(args.output, "w") as f:
            f.write(hex_key)
        print(f"The key is saved to a file: {args.output}")

if __name__ == "__main__":
    main()
