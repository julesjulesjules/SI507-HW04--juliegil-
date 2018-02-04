### 1/29/2018
### Magic Eight Ball Function

import random

eightball_answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
"You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
"Don't count on it", "My reply is no", "My sources say no", "Outlook is not so good", "Very doubtful"]

print("Welcome to the Magic Eight Ball game!")
print("Enter quit to exit")

person_q = input("What is your question?")

while person_q.lower() != "quit": 
  
  while "?" not in person_q: 
    person_q = input("I'm sorry, I can only answer questions... Please try again: ")
  
  person_q = input("What is your question?")
  
  print(random.choice(eightball_answers))
