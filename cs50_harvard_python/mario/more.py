def get_int_input(str_to_show):
    try:
        var = int(input(str_to_show))
        if(var > 0 and var < 23):
            return var
        else:
            str_to_show = "Enter between 0-23: "
            return get_int_input(str_to_show)
    except:
        str_to_show = "sorry, try again: "
        return get_int_input(str_to_show)

def main():
    height = get_int_input("Enter a height: ")
    for i in range(2,height+2):
        print((height-i+1)*" ", i*"#", i*"#")

if __name__ == "__main__":
    main()
    