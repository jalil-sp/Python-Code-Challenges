#Write the results of the code below to a txt file
#Using rad_to_deg from week 1



import math
def rad_to_deg():
    nbr_str = input("What do you want converted from radians to degrees (number only):")
    unconverted_nbr = int(nbr_str)
    pi = math.pi
    converted_nbr = round((unconverted_nbr*(180/pi)),2)

    with open('conversion_results.txt','a') as file:
        file.write(f"{unconverted_nbr} radians is equivalent to {converted_nbr} degrees\n")
    print("Conversion results written to 'conversion_results.txt'")

rad_to_deg()

'''
Potential Improvements:
-Ask user to specify th name of the output file that will be saved
-Print out the conversion in terminal

'''