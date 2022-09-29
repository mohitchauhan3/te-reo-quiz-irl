#27/06/2022
#Mohit Chauhan
#new learning 

#import the random library
import random

#globals and queston lists 
score = 0
english = ["Computer", "Lake", "Food", "New Zealand"]
right_answer = ["Rorohiko", "Roto", "Kai", "Aotearoa"]
option_1 = ["Kia Ora" , "Wrong Answer", "Wrong Answer", "test"]
option_2 = ["Slimbob" , "Wrong Answer", "Wrong Answer", "test"]

# define a function to generate a question
def generate_question(english,right_answer,option_1,option_2):
  global score
  print("What is the correct word for",english, "in maori")
  #Generate a random number to determine the sequence of question
  random_sequence = random.randint(0,2)
#seperate print statements for readability
  if(random_sequence == 0):
    print("A", option_1)
    print("B", option_2)
    print("C", right_answer)
    answer = input().lower()
    if answer == "c":
      score += 1
    else:
      print("incorrect.")
  
  
  elif(random_sequence == 1):
    print("A", right_answer)
    print("B", option_1)
    print("C", option_2)
    answer = input().lower()
    if answer == "a":
      score += 1
    else:
      print("incorrect.")
  
  
  elif(random_sequence == 2):
    print("A", option_1)
    print("B", right_answer)
    print("C", option_2)
    answer = input().lower()
    if answer == "b":
      score += 1
    else:
      print("incorrect.")
  
#generate 3 question pulling possible answer from list
for i in range (0,4):
  generate_question(english[i],right_answer[i],option_1[i],option_2[i])
  
#print the score at the end of the quiz 
print(score)
