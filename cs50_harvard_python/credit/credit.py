def get_int_input(str_to_show):
    try:
        var = int(input(str_to_show))
        return var
    except:
        str_to_show = "sorry, try again: "
        return get_int_input(str_to_show)

def main():
    cc_number = get_int_input("Number: ")
    tmp_cc_num = cc_number
    product_even = product_odd = 0
    invalid = 1
    for i in range(len(str(tmp_cc_num))-2, -1, -2):
        product_even += ((int(str(tmp_cc_num)[i]) * 2) % 10) + ((int(str(tmp_cc_num)[i]) * 2) // 10)
    
    for i in range(len(str(tmp_cc_num))-1, -1, -2):
        product_odd += (int(str(tmp_cc_num)[i]))

    if((product_even + product_odd) % 10 == 0):
        first_two = int(str(cc_number)[:2])
        if((len(str(cc_number)) == 15) and (first_two == 34 or first_two == 37)):
            print("AMEX")
            invalid = 0
        elif((len(str(cc_number)) == 16) and (first_two >= 51 and first_two <= 55)):
            print("MASTERCARD")
            invalid = 0
        elif((len(str(cc_number)) == 16 or len(str(cc_number)) == 13) and (first_two//10 == 4)):
            print("VISA")
            invalid = 0

    if(invalid != 0):
        print("INVALID")


if __name__ == "__main__":
    main()
