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

def get_letter_counts(word):
    result = dict()
    for c in word:
        result[c] = result.get(c, 0) + 1
    return result

def available_for_yellow(target_word, letter_counts, guess):
    green_counts = dict()
    for position, guess_letter in enumerate(guess):
        if target_word[position] == guess_letter:
            green_counts[guess_letter] = green_counts.get(guess_letter, 0) + 1

    available_for_yellow = {letter: count - green_counts.get(letter, 0) for letter, count in letter_counts.items()}
    print(available_for_yellow)
    return available_for_yellow

def inputCheck(guess, words, answers):
    while len(guess) !=5:
        guess = input("Enter a 5 letter guess: ").lower().strip()
    while guess.isalpha() == False:
        guess = input("Enter a guess with only letters: ").lower().strip()
    while guess not in words and guess not in answers:
        guess = input("Enter a valid word: ").lower().strip()
    return guess

boolean = True
i = 0

print("Welcome to Jake's wordle, good luck!")

while boolean == True:
    guess = input("Enter your guess: ")
    guess = guess.lower().strip()
    guess = inputCheck(guess, words, answers)
    i+=1
    target_word_letter_counts = get_letter_counts(answer)
    availability = available_for_yellow(answer, target_word_letter_counts ,guess)

    if guess==answer:
        print("Correct! It took you :", i, "tries")
        boolean = False
        continue
    
    for x in range(5):
        if guess[x] == answer[x]:
            print("Letter", guess[x], "is correct (green)")
        elif guess[x] in answer:
            if availability[guess[x]]> 0:
                print("Letter", guess[x], "is located in the answer (yellow)")
                availability[guess[x]] -=1
            else:
                print("Letter", guess[x], "is grey")
        else:
            print("Letter", guess[x], "is grey")