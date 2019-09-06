import math

def get_float_input(str_to_show):
    try:
        var = float(input(str_to_show))
        if(var > 0):
            return var
        else:
            str_to_show = "Must be > 0: "
            return get_float_input(str_to_show)
    except:
        str_to_show = "sorry, try again: "
        return get_float_input(str_to_show)

def main():
    change = get_float_input("Changes owed: ")
    change = math.floor(change*100)
    answer = 0
    coins = [25, 10, 5, 1]
    for i in range(4):
        while(change // coins[i] > 0):
            answer += 1
            change -= coins[i]

    print(answer)

if __name__ == "__main__":
    main()
    