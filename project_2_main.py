import random
import time
import pandas as pd
from playsound import playsound
from tkinter import messagebox
from tkinter import *

root = Tk()

hang = ["""
H A N G M A N 

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |2
 /    |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


# define function(list) in which random word will be selected
def fruit():
    words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot',
             'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']

    word = random.choice(words)
    return word


def car():
    words = ['honda', 'maruti', 'ferrari', 'bmw', 'audi', 'volvo', 'mahindra', 'tata',
             'hyundai', 'morris', 'skoda', 'kia', 'toyota', 'lamborgini', 'pagani']

    word = random.choice(words)
    return word


def anime():
    words = ['onepiece', 'demonslayer', 'bleach', 'naruto', 'dragonballz', 'attackontitan', 'castlevania', 'suzume',
             'onepunchman', 'spyfamily', 'rentagirlfriend', 'chainsawman']

    word = random.choice(words)
    return word

def indian_actresses():
    words = ["deepikapadukone", "priyankachopra", "katrinakaif", "kanganaranaut", "aliaabhatt", "anushkasharma", "kareenakapoor",
             "dishapatani", "shraddhakapoor","madhuridixit","tamannabhatia","kritisanon","yamigautam","shrutihassan",
        "dishapatani","kiaraadvani","janhvikapoor","sarahalikhan","ananyapandey","mrunalthakur"]
    word = random.choice(words)
    return word

def indian_actors():
    words = ["shahrukhkhan","salmankhan","aamirkhan","akshaykumar","amitabhbachchan","ranbirkapoor","hrithikroshan", "ranveersingh","varundhawan"
             ,"irrfankhan","shahidkapoor","ajaydevgan","sidharthmalhotra","kartikaaryan","sanjaydutt","emraanhashmi","sushantsinghrajput","vickykaushal",
             "rajkummarrao","nawazuddinsiddiqui","manojbajpayee"]
    word = random.choice(words)
    return word

def animals():
    words = ["dog","cat","elephant","lion","tiger","giraffe","monkey","zebra","kangaroo","panda","hippopotamus","cheetah","gorilla",
        "rhinoceros","rabbit","squirrel","dolphin","whale","bear","wolf","deer","penguin","parrot","ostrich","crocodile",
        "snake","frog","turtle","octopus","shark","rat","orangutan","buffalo",
        "snail","fox","bat"]
    word = random.choice(words)
    return word


# define the score board hang(list) and missedletters,secretword,correctletter"end='' The end parameter in the print function is used to add any string"
def displayBoard(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")


def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter or a word(spell the word correctly): ')
        guess = guess.lower()
        if len(guess) == len(secretWord): # if the input is a word
            return guess # return it as the guess
        elif len(guess) == 1: # if the input is a letter
            if guess in alreadyGuessed:
                print('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a LETTER.')
            else:
                return guess
        else: # if the input is neither a letter nor a word
            print('Please enter a single letter or a word.')


def playAgain():
    return input("\nDo you want to play again? ").lower().startswith('y')


missedLetters = ''
correctLetters = ''

player_times = {}
while True:
    print('Hello there!! Select the catagory in which you want to play ')
    print("Options:")
    print("Enter '1' for anime")
    print("Enter '2' for car")
    print("Enter '3' for fruit")
    print("Enter '4' for indian_actresses")
    print("Enter '5' for indian_actors")
    print("Enter '6' for animal")
    
    user = input("operation: ")

    if user == "1":
        secretWord = anime()
        break
    elif user == "2":
        secretWord = car()
        break
    elif user == "3":
        secretWord = fruit()
        break
    elif user == "4":
        secretWord = indian_actresses()
        break
    elif user == "5":
        secretWord = indian_actors()
        break
    elif user == "6":
        secretWord = animals()
        break
        # Initialize game start time
gameIsDone = False
start_time = time.time()

def HideAllFrames(x):
    for widget in x.winfo_children():
        widget.destroy()

while True:
    displayBoard(hang, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if len(guess) == len(secretWord): # if the guess is the whole word
        if guess == secretWord:
            game_time = end_time - start_time  # Calculate game duration    
            playsound('C:\PYTHON\python_project\spiderman-2099-theme-[AudioTrimmer.com].mp3')    
            player_name = input("Enter your name: ")
            player_times[player_name] = game_time  # Store player's name and game time in the dictionary
            messagebox.showinfo('Game Status', 'You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                    str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
        elif guess != secretWord:
                displayBoard(hang, missedLetters,
                         correctLetters, secretWord)               
                playsound('C:\PYTHON\python_project\pacman_audio1.mp3')            
                messagebox.showinfo('Game Status', 'You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True
            
                    
    elif guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            game_time = end_time - start_time  # Calculate game duration
            
            playsound("C:\PYTHON\python_project\spiderman-2099-theme-[AudioTrimmer.com].mp3")
            
            player_name = input("Enter your name: ")
            player_times[player_name] = game_time  # Store player's name and game time in the dictionary
            messagebox.showinfo("Game Status", '\nYes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hang) - 1:
            displayBoard(hang, missedLetters,
                         correctLetters, secretWord)
            playsound('C:\PYTHON\python_project\pacman_audio1.mp3')            
            messagebox.showinfo("Game Status", 'You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
    end_time = time.time()  # Get game end time

    if gameIsDone:        
        root.title("Time Data") #window title
        root.geometry("400x400") #window size
        time_frame = LabelFrame(root, bd=2, relief="groove", bg="white", fg="black")
        time_frame.place(x = 25, y = 25, width = 350, height = 350)
        
        time_label1 = Label(time_frame, text="LEADERBOARD", font="arial 20 bold ", bg="white", fg="red").grid(row=0, column=2)

        if len(player_times)>1:
            time_label2 = Label(time_frame, text = f'{list(player_times.keys())[-1]}: {list(player_times.values())[-1]:.2f} seconds', font="arial 20 bold italic", bg="white", fg="black").grid(row=2, column=2)
        else:
            for player, time_taken in player_times.items():
                time_label2 = Label(time_frame, text = f'{player}: {time_taken:.2f} seconds', font="arial 20 bold italic", bg="white", fg="black").grid(row=2, column=2)
        
        df = pd.DataFrame(list(player_times.items()), columns=['Player','Time (sec)'])
        # Sort the DataFrame by 'Time (seconds)' column in ascending order
        sorted_df = df.sort_values(by='Time (sec)')
        #time_label3 = Label(time_frame, text = "Player Times:", font="arial 20 bold italic", bg="white", fg="blue").grid(row=5, column=2)
        
        time_label4 = Label(time_frame, text = sorted_df, font="arial 20 bold italic", bg="white", fg="black").grid(row=6, column=2)        
        if playAgain():
            HideAllFrames(time_frame)
            start_time = time.time()
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            while True:
                print('Hello there!! Select the catagory in which you want to play ')
                print("Options:")
                print("Enter '1' for anime")
                print("Enter '2' for car")
                print("Enter '3' for fruit")
                print("Enter '4' for indian_actresses")
                print("Enter '5' for indian_actors")
                print("Enter '6' for animal")
    
                user = input("operation: ")

                if user == "1":
                    secretWord = anime()
                    break
                elif user == "2":
                    secretWord = car()
                    break
                elif user == "3":
                    secretWord = fruit()
                    break
                elif user == "4":
                    secretWord = indian_actresses()
                    break
                elif user == "5":
                    secretWord = indian_actors()
                    break
                elif user == "6":
                    secretWord = animals()
                    break
        else:
            break
