import string

in_str = input("Please enter your input: ")
shift_key = 4
letters = list(string.ascii_lowercase)

ltn = { letters[i]: i for i in range(len(letters)) }
ntl = { i: letters[i] for i in range(len(letters)) }

def encrypt(text, shift):
    """Encrypt the given lowercase-alphabetic + whitespace text with the shift key."""
    result = ""
    for ch in text:
        if ch in ltn:
            orig_index = ltn[ch]
            new_index  = (orig_index + shift) % 26
            result += ntl[new_index]
        else:
            # leave whitespace or non-lowercase unchanged
            result += ch
    return result

def decrypt(ciphertext, shift):
    """Decrypt the ciphertext (assuming it was produced with encrypt above) using the shift key."""
    result = ""
    for ch in ciphertext:
        if ch in ltn:
            orig_index = ltn[ch]
            new_index  = (orig_index - shift) % 26
            result += ntl[new_index]
        else:
            result += ch
    return result

# Run encryption
cipher = encrypt(in_str, shift_key)
print("Encrypted text:", cipher)

# Run decryption
plain  = decrypt(cipher, shift_key)
print("Decrypted text:", plain)
