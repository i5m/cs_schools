def get_int_input(str_to_show):
    try:
        var = int(input(str_to_show))
        return var
    except:
        return get_int_input(str_to_show)

def main():
    annual_salary = get_int_input("Annual Salary: ")
    portion_saved = get_int_input("Percentage saved per month out of 100: ")
    total_cost = get_int_input("Total cost of house: ")
    semi_annual_raise = get_int_input("Enter the semi­annual raise out of 100: ")
    portion_down_payment = total_cost / 4
    current_savings = 0
    r = 0.04 # return
    months_req = 0
    while(portion_down_payment >= current_savings):
        current_savings += ((portion_saved/100)*annual_salary/12) + (current_savings * r/12)
        months_req += 1
        if(months_req % 6 == 0):
            annual_salary += annual_salary * semi_annual_raise / 100
    print("Number of months: ", months_req)

if __name__ == "__main__":
    main()
