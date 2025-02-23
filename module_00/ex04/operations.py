import sys

def usage():
    print("python3 operationsp.py <integer1> <integer2>")

if len(sys.argv) == 1:
    usage()
    sys.exit(1)
elif len(sys.argv) == 2:
    print("AsertionError: not enough arguments")
    usage()
    sys.exit(1)
elif len(sys.argv) > 3:
    print("AssertionEsor: too many arguments")
    usage()
    sys.exit(1)
else:
    try:
        number1 = int(sys.argv[1])
        number2 = int(sys.argv[2])
        text_sum = number1 + number2
        text_diff = number1 - number2
        text_prod = number1 * number2
        if (number2 != 0):
            text_quot = number1 / number2
            text_remain = number1 % number2
        else:
            text_quot = "ERROR (division by zero)"
            text_remain = "ERROR (modulo by zero)"
        text = f"""
        Sum: {text_sum}
        Difference: {text_diff}
        Product: {text_prod}
        Quotient: {text_quot}
        Remainder: {text_remain}"""
        print(text)
    except ValueError:
        print("AssertionError: only integers")
        sys.exit(1)



