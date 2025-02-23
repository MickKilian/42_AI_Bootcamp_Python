import sys

# Morse code dictionary for alphanumeric characters
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

def encode_to_morse(input_string):
    # Ensure it's uppercase as Morse code is case insensitive
    input_string = input_string.upper()  
    
    # Check for invalid characters
    for char in input_string:
        if char not in MORSE_CODE_DICT:
            return "ERROR"  # Return "ERROR" if any invalid character is found

    # Convert valid input to morse code
    morse_code = [MORSE_CODE_DICT[char] for char in input_string]

    return ' '.join(morse_code)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 morse_code.py <string_to_encode>")
        return
    
    # Join all arguments into a single string separated by a space
    input_string = " ".join(sys.argv[1:])
    
    # Get the Morse code equivalent of the input string
    morse_string = encode_to_morse(input_string)
    
    if morse_string == "ERROR":
        print("ERROR")
    else:
        print(morse_string)

if __name__ == "__main__":
    main()
