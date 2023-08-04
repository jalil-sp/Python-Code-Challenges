import math
def rad_to_deg():
    nbr_str = input("What do you want converted from radians to degrees (number only):")
    unconverted_nbr = int(nbr_str)
    pi = math.pi
    converted_nbr = round((unconverted_nbr*(180/pi)),2)
    print(unconverted_nbr, "radians is equivalent to", converted_nbr, "degrees")
rad_to_deg()