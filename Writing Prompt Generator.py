import time, sys, random, os


#FUNCTIONS
def pullPrompt(list):
    prompt = random.choice(list)
    print(prompt)

def clearScreen():
    os.system("clear")


#PROMPT LIBRARY
fant_prompt = [ 
    "Story with the line: magic comes at a cost: are you willing to pay it?", 
    "Thief gets hired to steal an unusual treasure", 
    "Thief runs into ex on the job",
    "Write about a sentient object",
    "Write a story where the brave knight doesn't want to kill the dragon",
    "Your character makes a living faking psychic powers. One day, they wake up with real powers",
    "Your character has an average job - with a touch of magic",
    "Luck is a hereditary trait",
    "They were muttering gibberish as they worked, unaware that they were about to cast a spell"
]

para_prompt = [
    "You got on the wrong bus and end up in a town where everything seems a little off",
    "There's something wrong with those woods - what is it?",
    "Story that starts with: 'Everyone was ready for the ritual'",
    "Write a story that involves a reflection in a mirror",
    "You're a photographer who specializes in spirit photography",
]

scifi_prompt = [
    "Write about a road trip 300 years in the future",
    "You can buy a pill that lets you pick what you will dream about",
    "Your hand clenches tightly around the device in your pocket",
    "I remember the last spring. It was eighteen years ago",
]

hist_prompt = [
    "Your character is part of a major historical event",
    "Write a story that takes place in the same building, but in two different time periods",
    "Write about a family dinner in the past",
    "'You had one job,' he said to the messenger who had just failed spectacularly"
]



#PROGRAM FUNCTION
writing = True

print("Welcome to the writing prompt generator!")
time.sleep(3.00)
clearScreen()

while writing == True:
    print("What genre are you writing? Your choices are: \n Fantasy \n Science Fiction \n Paranormal/Horror \n Historical Fiction ")
    time.sleep(3.00)
    pull_prompt = str.lower(input("Type your genre:   "))
    picking = True
    while picking == True:
        if pull_prompt == "fantasy":
            pullPrompt(fant_prompt)
            picking = False
        elif pull_prompt == "paranormal" or pull_prompt == "horror":
            pullPrompt(para_prompt)
            picking = False
        elif pull_prompt == "science fiction" or pull_prompt == "scifi" or pull_prompt == "sci fi":
            pullPrompt(scifi_prompt)
            picking = False
        elif pull_prompt == "historical":
            pullPrompt(hist_prompt)
            picking = False
        else:
            print("Invalid genre - please try again.")
            time.sleep(3.00)
            pull_prompt = str.lower(input("Type your genre:   "))

        if picking == False:
            break
    
    time.sleep(3.00)
    keepWriting = int(input("Would you like another prompt? Enter 1 for yes, or 2 for no:   "))
    if keepWriting == 2:
        writing = False
    else:
        clearScreen()

    if writing == False:
        break

print("See you later!")
time.sleep(3.00)
sys.exit()