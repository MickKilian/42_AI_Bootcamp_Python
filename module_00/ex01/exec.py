import sys

if len(sys.argv) < 2:
    print("Usage: python3 exec.py <arg1> <arg2> <arg3> ...")
else:
    newstr = ""
    for idx, arg in enumerate(sys.argv[1:]):
        for i in range(len(arg)):
            newstr += arg[i].swapcase()
        if idx < len(sys.argv[1:]) - 1:
            newstr += " "
    print(newstr)


