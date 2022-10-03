#!/usr/bin/env python3
""" Prints out a list of employees for a user-selected fruit company. """

def main():
    """ Saves user-input fruit company & prints a list of employees """

    fruitcompanies= [{"name":"Zesty","employees":["Brian", "Colin", "Derik", "Emily", "Fortune"]},
                     {"name":"Ripe.ly","employees":["Kishor", "Leia", "Maria", "Jason"]},
                     {"name":"FruitBee","employees":["Monte", "Jarrad", "Pemba", "Don"]},
                     {"name":"HoneyGrove","employees":["Tim", "Travis", "Trung", "Torin"]}]

    # flag to track whether user-entered company exists
    match_flag = None

    while not match_flag:
        usr_company = input("Please choose a company (Zesty, Ripe.ly, FruitBee, HoneyGrove): ")


        # loop over the company dicts in the list
        for company in fruitcompanies:

            # find the matching company
            if company['name'].lower() == usr_company.lower():
            
                # update match flag value
                match_flag = "yes"

                print(f"\n{usr_company} Employees: ")
            
                # loop over employee list
                for employee in company['employees']:
                
                    # Jason is dead to us
                    if employee != "Jason":
                    
                        print(employee)

        # message if no matching company was found
        if not match_flag:
            print(f"\nCould not find the company name you entered. Please try again.\n")

    print("")






main()
