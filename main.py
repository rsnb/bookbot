import sys

def count_characters(s: str) -> dict[str, int]:
    lowered_string = s.lower()
    counts: dict[str, int] = {}
    for c in lowered_string:
        counts[c] = counts.get(c, 0) + 1
    return counts

def count_words(s: str) -> int:
    return len(s.split())

def main():
    file_name = "books/frankenstein.txt"
    with open(file_name) as f:
        file_contents = f.read()
    print(f"---Begin report of {file_name} ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()
    counts = count_characters(file_contents)
    sorted_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)
    for character, count in sorted_counts:
        if character.isalpha():
            print(f"The '{character}' character was found {count} times")
    print(f"---End report ---")
    return 0

if __name__ == "__main__":
    sys.exit(main())
