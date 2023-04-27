

def is_even(num):
    return num % 2 == 0


# write a slogify function which slugifies a given string
# by lowering the letters, stripping spaces at the beginning and end, and replacing empty space with dashes

def slugify(string):
    return string.lower().strip().replace(" ", "-")
    

slugify("ABRA CADABRA ARRG")

# Write code that counts the vowels in a word

def count_vowels(word):
    count = 0

    for char in word:
        if char in "aeiou":
            count +=1
    return count
