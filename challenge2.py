ciphertext_hex = "2c11130b59130b591b582a1f1b0b1f0c59371d0a09191e1f"

bytes_list = [ciphertext_hex[i:i+2] for i in range(0, len(ciphertext_hex), 2)]
formatted_bytes = [f'0x{byte}' for byte in bytes_list]

print(formatted_bytes)