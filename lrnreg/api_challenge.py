#!/usr/bin/env python3

import requests
import random

URL = "https://opentdb.com/api.php?amount=10&category=20&difficulty=medium"

def main():

    data = requests.get(URL).json()

    #print(data.get("results"))

    for question_dict in data.get("results"):
	
        print(question_dict["question"])
	
        idx = random.randint(0, 3)
	
        answers = question_dict["incorrect_answers"]
        
        answers.insert(idx, question_dict["correct_answer"])
	
        labels = ["A", "B", "C", "D"]

        correct_choice = labels[idx]

        for pos, choice in enumerate(labels):

            print(f"{choice}. {answers[pos]}")

        usr_choice = input("Your answer: ").upper()

        if usr_choice == correct_choice:
            print("Success!")

        else:
            print(f"Terrible!\nThe correct answer was {correct_choice}. {answers[idx]}") 

	
if __name__ == "__main__":
	main()
