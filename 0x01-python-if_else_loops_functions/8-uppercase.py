def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)  # Convert to uppercase using ASCII values
        else:
            uppercase_char = char
        print(uppercase_char, end="")
    print()  

