import sys
from stats import word_count, char_count, sort_on


def get_book_text(book_path: str) -> str:
    with open(book_path, encoding="utf-8") as f:
        return f.read()


def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)

    
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")

    
    print("--------- Character Count -------")
    counts = char_count(text)
    for ch, n in sort_on(counts):
        print(f"{ch}: {n}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
