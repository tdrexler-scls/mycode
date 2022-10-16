#!/usr/bin/env python3

import requests
import random

URL = "https://opentdb.com/api.php?amount=10&category=20&difficulty=medium"

def main():


	data = requests.get(URL).json()
	
	print(data.get("results"))
	
	for question_dict in data.get("results")):
		
		print(question_dict["question"])
		
		idx = random.randint(0, 3)
		
		answers = question_dict["incorrect_answers"].insert(idx, question_dict["correct_answer"])
		
		for position, choice in enumerate(["A", "B", "C", "D"]):
		
			print(f"{choice}. {answers[position]}")
	
	
if __name__ == "__main__":
	main()