import sys
from lexer_runner import print_tokens

def main():
    if len(sys.argv) != 2:
        print("Usage: python src/main.py <path/to/file.sql>")
        sys.exit(1)

    print_tokens(sys.argv[1])

if __name__ == "__main__":
    main()
