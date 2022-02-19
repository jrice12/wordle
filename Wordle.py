import random

file = open("Documents\Python\wordle-allowed-guesses.txt", "r")

words = []
for line in file:
  stripped_line = line.strip()
  words.append(stripped_line)

file.close()

answer_file = open("Documents\Python\wordle-answers-alphabetical.txt", "r")

answers = []
for answer in answer_file:
  stripped_answer = answer.strip()
  answers.append(stripped_answer)

answer_file.close()

answer = random.choice(answers)
print(answer)

def inputCheck(guess, words, answers):
    while len(guess) !=5:
        guess = input("Enter a 5 letter guess: ").lower()
    while guess.isalpha() == False:
        guess = input("Enter a guess with only letters: ").lower()
    while guess not in words and guess not in answers:
        guess = input("Enter a valid word: ").lower()
    return guess

boolean = True
i = 0

print("Welcome to Jake's wordle, good luck!")

while boolean == True:
    guess = input("Enter your guess: ")
    guess = guess.lower()
    guess = inputCheck(guess, words, answers)
    i+=1
    tempString = []

    if guess==answer:
        print("Correct! It took you :", i, "tries")
        boolean = False
        continue

    for x in range(5):
        if guess[x] == answer[x]:
            tempString.append(guess[x])
            print("Letter", guess[x], "is correct (green)")
        elif guess[x] in answer:
            tempString.append(guess[x])
            if tempString.count(guess[x]) > answer.count(guess[x]):
                print("Letter", guess[x], "is grey")
            else:
                print("Letter", guess[x], "is located in the answer (yellow)")
        else:
            print("Letter", guess[x], "is grey")