encrypted = "Mrkq"
unencrypted = ""

for sigma in encrypted:
    old_number = ord(sigma)
    new_number = old_number - 3
    unencrypted += chr(new_number)

print(f"Расшифровано: {unencrypted}")
