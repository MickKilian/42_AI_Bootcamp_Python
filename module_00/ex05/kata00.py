kata = (19,42,21)
text = "The " + str(len(kata)) + " numbers are: "

for idx, num in enumerate(kata):
    text += str(num)
    if idx < len(kata) - 1:
        text += ", "

print(text)
