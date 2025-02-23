import sys
import string

def text_analyzer(arg=None):
    """
    This function counts the number of printable characters, upper-case characters, lower-case characters,
    punctuation characters and spaces in a string.

    Parameters:
    a single string argument.

    Returns:
    text with the total number of printable characters, and respectively :
    the number of upper-case characters, lower-case characters, punctuation characters and spaces.
    """
    if arg is None:
        print("What is the text to analyze ?")
        sys.exit(1)
    elif not isinstance(arg, str):
        print("AssertionError: argument is not a string.")
        sys.exit(1)
    else:
        count_print = 0
        count_upper = 0
        count_lower = 0
        count_punct = 0
        count_space = 0
        for i in range(len(arg)):
            if arg[i].isprintable():
                count_print += 1
                if arg[i].islower():
                    count_lower += 1
                elif arg[i].isupper():
                    count_upper += 1
                elif arg[i].isspace():
                    count_space += 1
                elif arg[i] in string.punctuation:
                    count_punct += 1
        text = f"""The text contains {count_print} printable character(s):
        - {count_upper} upper letter(s)
        - {count_lower} lower letter(s)
        - {count_punct} punctuation mark(s)
        - {count_space} space(s)"""
        print(text) 

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("What is the text to analyze ?")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("This programs needs only one string argument and no more.")
        sys.exit(1)
    else:
        text_analyzer(sys.argv[1])