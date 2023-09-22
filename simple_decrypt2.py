MyHexEncrypted = ['0x11', '0x03', '0x10', '0x17', '0x12']
#The Hex Values that have been encrypted with the string PASSWD.
XOR_KEY =   "PASSW"
#We have 5 Hex Values
#We have a 5 letter XOR key

Encrypted_Decimal_Values = []
#Create an Empty List

for i in MyHexEncrypted:
    Encrypted_Decimal_Values.append(int(i,16))
print(Encrypted_Decimal_Values)


#Loop through the HEX Values and convert them to decimal.

decrypted_values = []
#Create an empty list that will hold our decrypted values

for i in range(len(Encrypted_Decimal_Values)):
    decrypted_value = Encrypted_Decimal_Values[i] ^ ord(XOR_KEY[i])
    decrypted_values.append(decrypted_value)
    #XOR each encrypted decimal against the corresponding letter in our original XOR_KEY

print("Decrypted Values Decimal:", decrypted_value)

print()
#Create a line break for readability
print("PlainText String")
for i in decrypted_values:
    print(chr(i), end="")
    #Convert each decimal value to ascii using the chr() method