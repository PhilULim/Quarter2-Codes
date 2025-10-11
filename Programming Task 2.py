Distance = float(input("Input the distance in kilometers:"))
Rate = float(input("Input the rate per kilometer:"))

def rateperdist():
    moneyz = globals() ['Rate'] *globals() ['Distance']
    return moneyz

print("The amount will be", rateperdist(), "pesos")