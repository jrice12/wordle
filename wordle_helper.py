import random
import wordfreq as wf
import math

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

possible_words = answers + words
boolean = True

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
    return available_for_yellow

while boolean == True:
    next_guess_value2 = 10000000
    string = []
    guess = input("Enter word guessed: ")
    temp_string = []
    for x in range(5):
        colour = input("Is the letter green, yellow, or grey ")
        temp_string.append(guess[x])
        if colour == "green":
            string.append(guess[x])
            
            for word in possible_words[:]:
                if guess[x] != word[x]:
                    possible_words.remove(word)
        if colour == "grey":
            for word in possible_words[:]:
                if temp_string.count(guess[x]) == guess.count(guess[x]) and guess[x] not in string and guess[x] in word:
                    possible_words.remove(word)
                elif guess[x] == word[x]:
                    possible_words.remove(word)
        if colour == "yellow":
            string.append(guess[x])
            for word in possible_words[:]:
                if string.count(guess[x]) > word.count(guess[x]):
                    possible_words.remove(word)
                elif guess[x] not in word:
                    possible_words.remove(word)
                elif guess[x] == word[x]:
                    possible_words.remove(word)

    print("There are ", len(possible_words), " words remaining")
    print("The remaining words are ", possible_words)
    new_words = []
    new_words = possible_words.copy()
    possible_answers = possible_words.copy()

    for word in possible_words[:]:
        guess = word
        total = 0
        possible_answers = new_words.copy()
        for answer in possible_answers[:]:
            possible_words = new_words.copy()
            target_word_letter_counts = get_letter_counts(answer)
            availability = available_for_yellow(answer, target_word_letter_counts ,guess)
            temp_string = []
            string = []
            if guess==answer:
                continue

            for x in range(5):
                if guess[x] == answer[x]:
                    colour = "green"
                elif guess[x] in answer:
                    if availability[guess[x]]> 0:
                        colour = "yellow"
                        availability[guess[x]] -=1
                    else:
                        colour = "grey"
                else:
                    colour = "grey"

                temp_string.append(guess[x])
                if colour == "green":
                    string.append(guess[x])
                    for word in possible_words[:]:
                        if guess[x] != word[x]:
                            possible_words.remove(word)
                if colour == "grey":
                    for word in possible_words[:]:
                        if temp_string.count(guess[x]) == guess.count(guess[x]) and guess[x] not in string and guess[x] in word:
                            possible_words.remove(word)
                        elif guess[x] == word[x]:
                            possible_words.remove(word)
                if colour == "yellow":
                    string.append(guess[x])
                    for word in possible_words[:]:
                        if string.count(guess[x]) > word.count(guess[x]):
                            possible_words.remove(word)
                        elif guess[x] not in word:
                            possible_words.remove(word)
                        elif guess[x] == word[x]:
                            possible_words.remove(word)
            total = total + len(possible_words)

        Expected_Remaining_Words = total/len(new_words)
        print(guess, " : ", Expected_Remaining_Words)
        print("Relative Frequency: ", wf.zipf_frequency(guess, "en"))
        value = (Expected_Remaining_Words+(math.log10(1/wf.word_frequency(guess, 'en', minimum=0.00000001))))/2
        temp_value = value
        if temp_value < next_guess_value2:
            next_guess_value2 = temp_value
            next_guess2 = guess
            Next_Guess_Remaining_Words=Expected_Remaining_Words

    print("The suggested next guess is: ", next_guess2, " with an expected remaining words of: ", Next_Guess_Remaining_Words)
    var = input("Would you like to quit? yes to quit, anything else to continue ")
    if var == "yes":
        boolean = False