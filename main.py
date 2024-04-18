import os


BOOK_DIRECTORY = "books"


def count_letters(text: str) -> dict[str, int]:
    lowered_text = text.lower()

    letter_count = dict()
    for ascii_char in range(97, 123):
        letter_count.update({chr(ascii_char): 0})

    for char in lowered_text:
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1

    return letter_count


def count_words(text: str) -> int:
    return len(text.split())


def generate_report(file_contents: str) -> str:
    word_count   = count_words(file_contents)
    letter_count = count_letters(file_contents)

    report = f'{word_count:,} words were found in the document.\n\n'

    for char, count in letter_count.items():
        report = f"{report}The letter '{char}' was found {count:,} time{'s' if count > 1 else ''}\n"
    
    return report


def main() -> None:
    for filename in os.listdir(BOOK_DIRECTORY):
        file = os.path.join(BOOK_DIRECTORY, filename)

        with open(file) as f:
            file_contents = f.read()

        print(f'--- Analysis of {file} ---')
        print(generate_report(file_contents))


if __name__ == '__main__':
    main()