def main():
    plaintext = input("plaintext: ")
    ciphertext = ""
    key = input("enter key: ")
    j = 0
    for i in plaintext:
        ascii_val = ord(i)
        if i.isalpha():
            if i.isupper():
                num_key = ord(key[j]) - 65
            else:
                num_key = ord(key[j]) - 97
            ascii_val += num_key
            if j == len(key) - 1:
                j = -1
            j += 1
            if not chr(ascii_val).isalpha():
                ascii_val -= 26
        ciphertext += chr(ascii_val)

    print(ciphertext)

if __name__ == "__main__":
    main()
