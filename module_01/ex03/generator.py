import random

def generator(text, sep, option=None):
    # Check if the text argument is a string
    if not isinstance(text, str):
        yield "ERROR"
        return
    
    # Check if the option argument is valid
    valid_options = ['shuffle', 'unique', 'ordered', None]
    if option not in valid_options:
        yield "ERROR"
        return
    
    # Split the text into words based on the separator
    words = text.split(sep)
    
    # Apply the chosen option
    if option == 'shuffle':
        random.shuffle(words)
    elif option == 'unique':
        words = list(set(words))
    elif option == 'ordered':
        words.sort()
    
    # Yield the words
    for word in words:
        yield word

# Example 1: Shuffle option
text = "apple orange banana apple cherry banana"
sep = " "
print("Shuffle option:")
for word in generator(text, sep, 'shuffle'):
    print(word)

# Example 2: Unique option
text = "apple orange banana apple cherry banana"
sep = " "
print("\nUnique option:")
for word in generator(text, sep, 'unique'):
    print(word)

# Example 3: Ordered option
text = "apple orange banana apple cherry banana"
sep = " "
print("\nOrdered option:")
for word in generator(text, sep, 'ordered'):
    print(word)

# Example 4: No option provided (default behavior)
text = "apple orange banana apple cherry banana"
sep = " "
print("\nNo option provided:")
for word in generator(text, sep):
    print(word)

# Example 5: Invalid `text` (not a string)
text = 1.0  # Not a string
sep = "."
print("\nInvalid text (not a string):")
for word in generator(text, sep):
    print(word)

# Example 6: Invalid `option`
text = "apple orange banana"
sep = " "
print("\nInvalid option:")
for word in generator(text, sep, 'invalid_option'):
    print(word)
