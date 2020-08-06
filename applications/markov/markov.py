import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

split_words = words.split()

dataset = {}
for i in range(len(split_words) -1):
    word = split_words[i]
    next_word = split_words[i+1]

    if word in dataset:
        dataset[word].append(next_word)
    else:
        dataset[word] = [next_word]


# TODO: analyze which words can follow other words
# Your code here

stop_signs = ('.', '?', '!')

def generate_sentence(word):
    print(word, end=" ")

    if word.endswith(stop_signs):
        print('\n')
        return
    else:
        generate_sentence(random.choice(dataset[word]))


# TODO: construct 5 random sentences
# Your code here

generate_sentence('One')
generate_sentence('The')
generate_sentence('Only')
generate_sentence('But')
generate_sentence('The')