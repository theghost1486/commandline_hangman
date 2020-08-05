import random
from wordlist import words
from os import system
from time import sleep


def getword():
 word = random.choice(words)
 word = word.upper()
 return word

def slowprint(text):
  for i in text:
    print(i,end="",flush=True)
    sleep(0.1)


def play(word):
  dashes = '_'*len(word)
  state = False
  letters_guessed = []
  words_guessed = []
  tries = 6
  slowprint("Welcome to hangman")
  print("\n")
  slowprint("This porject has been made by Ansh Pandya")
  print("\n")
  slowprint("Press enter to continue")
  input()
  system("clear")  
  while not state and tries > 0:
    letters_remaining = 0
    for i in dashes:
      if i == "_":
        letters_remaining+=1
    system("clear")
    print(display_hangman(tries))
    print(dashes)
    print("No of letters remaining are:{}".format(letters_remaining))
    ui = input("Enter your guess:").upper()
    if len(ui) == 1 and ui.isalpha():
      if ui in letters_guessed:
        print("you have already guessed the letter")
      elif ui not in word:
        print("The letter is not in the word")
        tries-=1
        letters_guessed.append(ui)
      else:
        print("The letter is in the word.")
        letters_guessed.append(ui)
        incomplete_word = list(dashes)
        indices = [i for i,letter in enumerate(word) if letter == ui]
        for index in indices:
          incomplete_word[index] = ui
        dashes = "".join(incomplete_word)
        if "_" not in dashes :
          state = True 
        
    elif len(ui) == len(word) and ui.isalpha():
      if ui in words_guessed:
        print("You have already guessed the word")
      elif ui != word:
        print("the word is incorrect")
        tries-=1
        words_guessed.append(ui)
      else:
        state = True
        dashes = word
    
    else:
      print("There seems to be an error")
  if state:
    print("you have guessed the word correctly")
  else:
    print("Sorry you ran out of tries")
    print("the correct word was {}".format(word))

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
  word = getword()
  play(word)
  while input("Pay again ? (Y/N)").upper() =="Y":
    word = getword()
    play(word)
  


if __name__ == "__main__":
  main()



