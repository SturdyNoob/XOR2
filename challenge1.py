Hex_Encrypted = ['0x0c', '0x3b', '0x13', '0x2d', '0x23', '0x2a', '0x2f', '0x16', '0x26', '0x39', '0x36']
KEY = "ABC"
#Our two initial values include the encrypted Hex and the KEY of ABC

print("The Original Encryption:")
print(Hex_Encrypted)

Encrypted_Decimal_Values = []
#Create an Empty List

for i in Hex_Encrypted:
    Encrypted_Decimal_Values.append(int(i,16))
    #Convert the hex into regular numbers and store them onto Encrypted_Decimal_Values

print(Encrypted_Decimal_Values)

decrypted_values = []
for position, value in enumerate(Encrypted_Decimal_Values):
    decrypted_value = value ^ ord(KEY[position % len(KEY)])
    decrypted_values.append(decrypted_value)

for i in decrypted_values:
    print(chr(i), end="")