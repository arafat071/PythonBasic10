
def tk_to_rupee(rupee_conversion_rate):
    user_input = float(input("Enter TK you want to convert in Rupee: "))
    result = float(user_input * rupee_conversion_rate)
    print("Your Rupee is: " + str(result))


tk_to_rupee(0.88)


def rupee_to_dollar():
    dollar_conversion_rate = .012
    user_input = float(input("Enter Rupee you want to convert in dollar: "))
    result = float(user_input * dollar_conversion_rate)
    print("Your Dollar is: " + str(result))


#rupee_to_dollar()


def tk_to_dollar():
    dollar_conversion_rate = .0092
    user_input = float(input("Enter TK you want to convert in dollar: "))
    result = float(user_input * dollar_conversion_rate)
    print("Your Dollar is: " + str(result))


#tk_to_dollar()

def tk_to_rupee():
    user_input1 = float(input("Enter Rupee conversion rate: "))
    user_input2 = float(input("Enter TK you want to convert in Rupee: "))
    result = float(user_input1 * user_input2)
    print("Your Rupee is: " + str(result))


#tk_to_rupee()