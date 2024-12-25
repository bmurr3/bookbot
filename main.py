import os

path = os.path.join(
    os.curdir,
    'books',
    'frankenstein.txt'
)

with open(path) as f:
    contents = f.read()

contents = contents.lower()
char_count: dict[str, int] = {}

for char in contents:
    if not char in char_count:
        char_count[char] = 0
    char_count[char] += 1

sorted_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
print(f'-- Beginning of report for {path} --')
print(f' Word Count: {len(contents.split())}')
print()
for key, value in sorted_count:
    print(f" > The character '{key}' was used {value:,} times.")
