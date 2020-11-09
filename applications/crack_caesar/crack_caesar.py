# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

most_freq = (
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",   
)

with open("ciphertext.txt") as f:
    text = f.read()

words = text.split()

letter_counts = {}

for word in words:
    for char in word:
        if char.isalpha():
            if char not in letter_counts:
                letter_counts[char] = 1
            else:
                letter_counts[char] += 1
        else:
            continue

letter_counts_list = list(letter_counts.items())
letter_counts_list.sort(key = lambda pair: pair[1], reverse=True)

# print(letter_counts_list)

keys = {}

for i in range(len(letter_counts_list)):
    keys[letter_counts_list[i][0]] = most_freq[i]

# print(keys)

def crack_code(s):
    new_str = ''

    for char in s:
        if char.isalpha():
            new_str += keys[char]
        else:
            new_str += char
    return new_str

decoded_words = map(crack_code, words)

print(" ".join(decoded_words))