import sys
from lexer_runner import print_tokens

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <file.sql> [--strict]")
        sys.exit(1)

    path = sys.argv[1]
    strict = "--strict" in sys.argv[2:]
    print_tokens(path, strict=strict)

if __name__ == "__main__":
    main()
