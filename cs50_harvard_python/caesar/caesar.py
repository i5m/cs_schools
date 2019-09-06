def get_int_input(str_to_show):
    try:
        var = int(input(str_to_show))
        return var
    except:
        str_to_show = "sorry, try again: "
        return get_int_input(str_to_show)

def main():
    plaintext = input("plaintext: ")
    ciphertext = ""
    key = get_int_input("enter key: ")
    for i in plaintext:
        ascii_val = ord(i)
        if i.isalpha():
            ascii_val += key
            if not chr(ascii_val).isalpha():
                ascii_val -= 26
        ciphertext += chr(ascii_val)

    print(ciphertext)

if __name__ == "__main__":
    main()
