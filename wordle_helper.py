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

while boolean == True:
    next_guess_value2 = 10000000
    string = []
    guess = input("Enter word guessed: ")
    for x in range(5):
        colour = input("Is the letter green, yellow, or grey ")
        if colour == "green":
            string.append(guess[x])
            for word in possible_words[:]:
                if guess[x] != word[x]:
                    possible_words.remove(word)
        if colour == "grey":
            #Grey letters before the green in words w repeating letters
            for word in possible_words[:]:
                if guess[x] in word and guess[x] not in string:
                    possible_words.remove(word)
                elif guess[x] in string and word.count(guess[x]) > 1:
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
            string=[]
            tempString = []
            if guess==answer:
                continue

            for x in range(5):
                if guess[x] == answer[x]:
                    tempString.append(guess[x])
                    colour = "green"
                elif guess[x] in answer:
                    tempString.append(guess[x])
                    if string.count(guess[x]) > word.count(guess[x]):
                        colour = "grey"
                    else:
                        colour = "yellow"
                else:
                    colour = "grey"

                    
                if colour == "green":
                    string.append(guess[x])
                    for word in possible_words[:]:
                        if guess[x] != word[x]:
                            possible_words.remove(word)
                if colour == "grey":
                    for word in possible_words[:]:
                        if guess[x] in word and guess[x] not in string:
                            possible_words.remove(word)
                if colour == "yellow":
                    string.append(guess[x])
                    for word in possible_words[:]:
                        #if string.count(guess[x]) > word.count(guess[x]):
                            #possible_words.remove(word)
                        if guess[x] not in word:
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