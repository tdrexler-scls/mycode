#!/usr/bin/env python3
""" Exercise using lists, input(), print() """

import random

def main():
    """ Selects a name from a list based on user input. """


    wordbank=["indentation", "spaces"]

    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", 
            "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach", "Ted"]

    wordbank.append(4)

    num = input(f"Please enter a number between 1 and {len(tlgstudents)}: ")

    num = int(num)

    # rand_num = random.randint(0, len(tlgstudents)-1)
    # student_name = tlgstudents[rand_num]

    student_name = tlgstudents[num-1]

    print(student_name, "always uses", wordbank[-1], wordbank[-2], "to indent.")



main()
