def summation():
    number1 = 10;
    numnber2 = 20;
    sum = number1 + numnber2
    print(sum)


# summation()


def subtraction():
    number1 = 10;
    numnber2 = 20;
    sum = number1 - numnber2
    print(sum)


# subtraction()


def multiply():
    number1 = 10;
    numnber2 = 20;
    sum = number1 * numnber2
    print(sum)


# multiply()


def division():
    number1 = 10;
    numnber2 = 20;
    sum = number1 / numnber2
    print(float(sum))


# division()


def dhaka():
    print("Dhaka")
    print("PnT")


# dhaka()


def tk_to_rupee():
    rupee_conversion_rate = .85
    user_input = float(input("Enter TK you want to convert in Rupee: "))
    result = float(user_input * rupee_conversion_rate)
    print("Your Rupee is: " + str(result))


tk_to_rupee()


def rupee_to_dollar():
    dollar_conversion_rate = .012
    user_input = float(input("Enter Rupee you want to convert in dollar: "))
    result = float(user_input * dollar_conversion_rate)
    print("Your Dollar is: " + str(result))


rupee_to_dollar()


def tk_to_dollar():
    dollar_conversion_rate = .0092
    user_input = float(input("Enter TK you want to convert in dollar: "))
    result = float(user_input * dollar_conversion_rate)
    print("Your Dollar is: " + str(result))


tk_to_dollar()

