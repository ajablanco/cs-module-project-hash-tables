def word_count(s):
    count = {}
    sentence = s.split()
    ignored = {'"', ':', ';', ',', '.', '-', '+', '=', '/',
               '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '\\'}


    for el in range(len(sentence)):
        strip_word = ""
        for char in range(len(sentence[el])):
            if sentence[el][char] not in ignored:
                strip_word += sentence[el][char]
        sentence[el] = strip_word.lower()
        
    for word in sentence:
        if word == "":
            return {}
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count 



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))