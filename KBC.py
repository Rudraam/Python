# lets make a game like KBC
#use data list type, for storing questions and answers
#display winning amount
import time
print("Deviyon Aur Sajannon!!!!")
print("===================================================================================")
print("Welcome to Kaun Banega Crorepati(Who will become a Crorepati?), hosted by Rudra ")
print("**************************Prize win in INR*****************************************")
print("===================================================================================")
print("Lets play this game. There will be three questions you have to answer")
tim = time.strftime("%H:%M:%S")
print("Time: ", tim)
print("To begin the game, I would need your name")
print("===================================================================================")
name = input("Enter your name: ")
print(name, ", Welcome to this great game. Lets begin!!!")
print("===================================================================================")


choice1 = ["B"]
print("So Your first Question is for 1,50,000 rupees:")
print("Question 1: Who is the creator of Python programming language?")
print("A) Dennis Ritchie")
print("B) Guido Van Rossum")
print("C) Linus Torvalds")
print("D) Larry Wall")
ans1 = input("Enter your answer: ")
if ans1 in choice1:
    print("Hurrey!!! You are correct. You have won 1,50,000")
else:
    print("Sorry!!! You are wrong. You have lost 1,50,000.")
    print("===================================================================================")
    
choice2 = ["A"]
print("So Your second Question is for 70,00,000 rupees:")
print("Question 2: Which of the following is a British luxury car brand?")
print("A) Rolls Royce")
print("B) Ferrari")
print("C) Lamborghini")
print("D) Mercedes-Benz")
ans2 = input("Enter your answer: ")

if ans2 in choice2:
    print("Hurrey!!! You are correct. You have won 1,00,00,000 rupees")
else:
 print("Sorry!!! You are wrong. You have lost 1,00,00,000")

choice3 = ["B"]
print("So Your second Question is for 1,00,00,000 rupees:")
print("Question 3: Which of the following is a famous place in India?")
print("A) Luxemborg")
print("B) Agra")
print("C) Toronto")
print("D) Qatar")
ans3 = input("Enter your answer: ")

if ans3 in choice3:
    print("Hurrey!!! You are correct. You have won 1,00,00,000 rupees")
else:
 print("Sorry!!! You are wrong. You have lost 1,00,00,000")

choice4 = ["A"]
print("So Your second Question is for 2,00,00,000 rupees:")
print("Question 4: Which of the following is a famous monument in Canada?")
print("A) CN Tower")
print("B) Taj Mahal")
print("C) Pyramids")
print("D) Burj Khalifa")
ans4 = input("Enter your answer: ")

if ans4 in choice4:
    print("Hurrey!!! You are correct. You have won 1,00,00,000 rupees")
else:
 print("Sorry!!! You are wrong. You have lost 1,00,00,000")
print("Alright, so here are the results:")

#now will build the game logic for wining and total prize money
if ans1 in choice1:
   print("You have won 1,50,000 rupees")
   total_prize1 = 1,50,000
   print("Prize Money: ", total_prize1)
elif ans1 != choice1:
   print("You have lost 1,50,00,000 rupees")
   total_prize2 = 0
   print("Prize Money: ", total_prize2)
elif ans2 in choice2:
   print("You have won 70,00,000 rupees")
   total_prize3 = 71,50,000
   print("Prize Money: ", total_prize3)
elif ans2 != choice2 and ans1 in choice1:
   print("You have lost 70,00,000 rupees")
   total_prize4 = 1,50,000
   print("Prize Money: ", total_prize4)
elif ans3 in choice3:
   print("You have won 1,00,00,000 rupees")
   total_prize5 = 1,71,50,000
   print("Prize Money: ", total_prize5)
elif ans3 != choice3 and ans2 in choice2:
   print("You have lost 1,00,00,000 rupees")
   total_prize6 = 71,50,000
   print("Prize Money: ", total_prize6)
elif ans4 in choice4:
   print("You have won 2,00,00,000 rupees")
   total_prize7 = 3,71,50,000
   print("Prize Money: ", total_prize7)
elif ans4 != choice4 and ans3 in choice3:
   print("You have lost 2,00,00,000 rupees")
   total_prize8 = 1,71,50,000
   print("Prize Money: ", total_prize8)
else:
   print("Error")



   



