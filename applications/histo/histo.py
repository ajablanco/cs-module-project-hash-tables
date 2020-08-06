# Your code here
def draw_histo(s):
    with open(s) as f:
        v = f.read()
    

    words = [x.lower() for x in v.split()]

    word_count = {}

    for i in range(len(words)):
        new_word = ""
        for char in words[i]:
            if char.isalnum():
                new_word += char
        if new_word in word_count:
            word_count[new_word] += 1
        else:
            word_count[new_word] = 1

    sorted_dict = {k:v for k,v in sorted(word_count.items(), key=lambda item:item[1], reverse=True)}
    
    for key in sorted_dict:
        sorted_dict[key] = "#" * sorted_dict[key]
        print(key.ljust(20, " ") + sorted_dict[key])
    
draw_histo('robin.txt')



# list = ['hello', 'hi', 'world']

# for i in list:
#     print(i)

# for i in range(len(list)):
#     print(i)

# for i in range(len(list) - 1):
#     print(i)