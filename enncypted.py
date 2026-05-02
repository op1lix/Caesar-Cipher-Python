message = "John"
shift = 3
encrypted = ""

for char in message:

    num_code = ord(char)

    new_code = num_code +shift

    encrypted += chr(new_code)

print(f"Зашифровано: {encrypted}")