import string
import sys  # Import sys to access argv

def filter_words(s, n):
    # Remove punctuation from the string using str.translate
    table = str.maketrans('', '', string.punctuation)
    cleaned_s = s.translate(table)

    # Split the string into words, then filter based on the length of non-punctuation characters
    return [word for word in cleaned_s.split() if len(word) > n]

def main():
    if len(sys.argv) != 3:  # We expect exactly 2 arguments: the string and the integer
        print("ERROR")
        return

    try:
        # Get arguments from command line input
        s = sys.argv[1]
        n = int(sys.argv[2])

        # Get the list of filtered words
        result = filter_words(s, n)

        # Print the result
        print(result)

    except (ValueError, IndexError):
        print("ERROR")

# Ensure the program is run as the main script
if __name__ == "__main__":
    main()
