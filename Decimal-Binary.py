def decimal_to_binary(decimal_num):
    binary = ""
    exponent = 7
    #finding what it can fit into then repeating
    for i in range(8):
        if decimal_num >= 2**exponent:
            #Adding one and subtracting if it fits
            binary += "1"
            decimal_num -= 2**exponent
        else:
            binary += "0"

        #changing exponent
        exponent -= 1
    #printing
    return binary