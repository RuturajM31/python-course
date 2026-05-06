# Question: Looping and counting occurrences of a letter. 
# Encapsulate in a function count that takes a string and a letter.

def count(word, letter):
    """Returns how many times 'letter' appears in 'word'."""
    counter = 0

    for char in word:
        if char == letter:
            counter = counter+1

    return counter


# Example usage
word = input("Enter a word: ")
letter = input("Enter a letter: ")

print("Count:", count(word, letter))