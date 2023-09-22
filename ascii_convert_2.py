plaintext = "A"
password = "B"

ascii_decimal = ord(plaintext) ^ ord(password)

ascii_hex = hex(ascii_decimal)

print(ascii_hex)

ascii_decrypted = int(ascii_hex, 16) ^ ord(password)

print(ascii_decrypted)

print(chr(ascii_decrypted))