def binary_to_decimal(binary_str):
    decimal = 0
    exponent = 0
    #checking which are ones
    for i in range(7, -1, -1):
        if binary_str[i] == str(1):
            #adding their values to the total
            decimal += 2 ** exponent
        exponent += 1
    #printing
    return decimal