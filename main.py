# Intro
print("~ Tales of Old Hagen ~")
print("(A Work of Fiction)")
print()
print("You are new to the town of Old Hagen and are looking to get to know the townsfolk.")
print()
# Pick a story
print("You enter the town square, bustling with life, and single out a few friendly-looking people you'd like to meet:")
print("  A. A man asking for directions")
print("  B. A woman with her daughter counting flowers")
print("  C. A shopkeeper petting his cat")
storyChoice = input("Which person would you like to speak with? Please select option A, B, or C: ")
  # Story 1: Display Story
if(storyChoice == "A"):
  print()
  print("You make your way to the lost man who seems grateful someone's coming over.")
  print('"Hello!", he says. "I am new here and am trying to send this letter to my mom back in my home country, do you know where the post office is?"')
  print()
  # Story 1: Ask multiple choice question
  print("You're new to this town, too, but that doesn't mean you can't take a guess. Where will you tell him to go?")
  print("  A. Down the road")
  print("  B. Up the road")
  print("  C. Through the alleyway")
  print("  D. Out of town")
  direction = input("Please select option A through D: ")
    # Story 1: Good Ending
  if(direction == "B"):
    print()
    print("The man thanks you and heads down the road; you hope you told him the right direction.")
    print()
    print("~ Two Days Later ~")
    print()
    print('You are walking through the town square again and hear someone say "Hey you!" and you turn around to see the man, a smile on his face.')
    print('"Thanks for giving me directions the other day, I found the post office nice and easy! Also, I realised I never got your name. I am Teddy, what is your name?"')
    print()
    userName = input("Please enter your name: ")
    print()
    print(f'"Well, {userName}, pleasure to meet you. We should go to the pub sometime!"')
    print()
    print("You've made a new friend, congratulations!")
    print()
    print("~ Good End ~")
    # Story 1: Bad Ending
  if(direction == "D"):
    print()
    print('"Well okay... if you say so!" he replies. You see him head out of town and never see him again.')
    print()
    print("~ Bad End ~")
  else:
    print()
    print("The man thanks you and goes on his way. You don't know if he ever found the post office, but you sure hope he did.")
    print()
    print("~ Bad End ~")
  # Story 2: Display Story
if(storyChoice == "B"):
  print()
  print("As you're walking over, you notice the girl has a puzzled look on her face.")
  print('The mom notices you and says, "Maybe this nice person would like to help, do you want to ask them?"')
  print()
  # Story 2: Ask a value question
  print('"Yeah!" she replies. "Excuse me, how many flowers are there total if there are 4 pink flowers, 2 white flowers, and 7 yellow flowers?"')
  print()
  flowerCorrect = 4 + 2 + 7
  flowerAnswer = input("Please enter the number of flowers total: ")
  flowerAnswer = int(flowerAnswer)
    # Story 2: Good Ending
  if(flowerCorrect == flowerAnswer):
    print()
    print(f'"Oh yeah! There are {flowerAnswer} flowers here, thank you!" she says.')
    print("The girl goes back to her mom and tells her about how nice you were to help her. The mom guestures you to come over, and you do.")
    print()
    print('"Thanks for helping Nila with that. My name is Penelope, what is yours?"')
    userName = input("Please enter your name: ")
    print()
    print(f'"Nice to meet you, {userName}. It is great knowing there are such kind people around here. Where are you from?"')
    print()
    print("The two of your talk for a while and get to know each other. You've made a new friend, congratulations!")
    print()
    print("~ Good End ~")
    # Story 2: Bad Ending
  else:
    print()
    print(f'"Oh... are you sure? I thought there were {flowerCorrect} flowers here."')
    print()
    print("You count again, and sure enough she's right. You sprint away in embarrassment, never to show your face again.")
    print()
    print("~ Bad End ~")
  # Story 3: Display Story
if(storyChoice == "C"):
  print()
  print("You walk over to the old man working at a trinket shop; he's so focused on his cat that he doesn't notice you until you're right at the window.")
  print()
  print("Oh, hello there! You look like a new face, what's your name?")
  userName = input("Please enter your name: ")
  print()
  print(f'"Well, nice to meet you, {userName}. Here, let me introduce you to my cat, Goatimer. Say hi."')
  print()
  print("-the cat meows at you-")
  print()
  # Story 3: Ask question
  print('"Haha, quite the charmer, yeah? Cats are just the best, you agree?"')
  print()
  catFate = input("Do you agree? Please enter 'Yes' or 'No': ")
    # Story 3: Good Ending
  if(catFate == "Yes"):
    print()
    print('"You got that right! I knew we would get along! Let me tell you about the time he..."')
    print()
    print("The two of you talked for a while about Goatimer and his mischief, sharing laughs and getting to know each other along the way.")
    print()
    print("You've made a new friend, congratulations!")
    print()
    print("~ Good End ~")
    # Story 3: Bad Ending
  else:
    print()
    print('"Then scram!"')
    print("He leaves no room for any other conversation, and you're left dejected. You head home with your head down and no new friends.")
    print()
    print("~ Bad End ~")