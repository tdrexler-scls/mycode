#!/user/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # colect string input from the user
    user_input = input("Please enter an IPv4 IP address: ")

    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)

    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)

    # challenge 01
    vendor_name = input("Please enter the vendor name: ")
    print("The vendor name is:", vendor_name)

main()
