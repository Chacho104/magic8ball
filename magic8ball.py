# In this project, I will be writing a program that can
# answer any "Yes" or "No" question with a different
# fortune each time it executes

# Start by importing random for random number generation

import random

# Define a random number variable that returns a random number
# between 1 and 9, inclusive

random_number = random.randint(1, 9)

# Define variables for user input

name = "Jolly"
question = "Will I be massively wealthy?"

# Define variable for answer
answer = ""

# Assign answers to answer variable based on the random number

if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
else:
    answer = "Error"

# If user doesn't input a question, program should prompt user
# to ask a question
if question == "":
    print("Please ask a question")

# If user asks a question but doesn't input name
elif name == "":
    print("Question:", question)
    print("Answer", answer)

# If user inputs both question and name

else:
    print(name, "asks:", question)
    print("Answer:", answer)