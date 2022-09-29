#4.1
#10/06/2022
#Mohit Chauhan

print("Kia Ora Ko Wai Tou Ingoa? / meaning Hello What is your name?")
n = input()
print("Kia Ora / hello " + n )

import random

# Asking The user name in te Reo 
#is a Python quiz program to assist the user in learning Te Reo they are a total of 13 questions to be asked 
score = 0

#Question 1
english = ["New Zealand", "Hungry", "Auckland", "Love", "One", "Good Night", "Tribe", "Family", "Good Morning", "Goodbye", "Canoe"]
right_answer = ["Aotearoa", "Hiakai", "Tāmaki Makaurau", "Aroha", "tahi", "pō mārie", "Iwi", "Whānau", "Mōrena", "Ka kite anō", "Waka"]
option_1 = ["Tāmaki Makaurau", "Kai", "Aotearoa", "Whānau", "wha", "Kia ora", "Whānau", "tahi", "Kia ora", "Kia ora", "Tainui"]
option_2 = ["Te Whanganui-a-Tara", "Whāngai", "tauranga", "Tauoko", "rua", "Tēnā koe", "Aroha", "Aroha", "Kei te pai", "Kei te pai", "Aotea"]
option_3 = ["Christchurch", "Hākari", "Christchurch", "Awhi", "toru", "haere mai", "tahi", "tahi", "Tino", "Mōrena", "Ka kite anō"]
def generate_question(english,right_answer,option_1,option_2,option_3):
  global score
  print("What is the correct word for",english, "in maori")
  random_sequence = random.randint(0,2)
  if(random_sequence == 0):
    print("A", option_1)
    print("B", option_2)
    print("C", right_answer)
    print("D", option_3)
    answer = input().lower()
    if answer == "c":
      score += 1
    else:
      print("incorrect")


  elif(random_sequence == 1):
    print("A", right_answer)
    print("B", option_1)
    print("C", option_2)
    print("D", option_3)
    answer = input().lower()
    if answer == "a":
      score += 1
    else:
      print("incorrect.")



  elif(random_sequence == 2):
    print("A", right_answer)
    print("B", option_1)
    print("C", option_2)
    print("D", option_3)
    answer = input().lower()
    if answer == "a":
      score += 1
    else:
      print("incorrect.")



for m in range (0,11):
 generate_question(english[m],right_answer[m],option_1[m],option_2[m],option_3[m])

if score <= 1:
  print("Your total score is:", score, "- better luck next time")
elif score == 2:
  print("you total score is:", score, "- you went ok.")
elif score == 3:
  print("your total score is:", score, "- your doing well")
else:
  print("your total score is:", score, "- your amazing ")  

 