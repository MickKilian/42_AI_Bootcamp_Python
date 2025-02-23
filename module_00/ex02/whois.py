import sys

# Fonction pour afficher le message d'utilisation
def usage():
    print("Usage: python3 whois.py <integer>")

# Vérifie si un argment a été fourni
if len(sys.argv) > 2:
    printf("AssertionError: more than one argument is provided.")
    usage()
    sys.exit(1)

# Vérifie si l'argument est un entier
try:
    number = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer.")
    sys.exit(1)

# Vérifie si l'argument est impair, pair ou zéro
if number == 0:
    print("I'm Zero.")
elif number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")