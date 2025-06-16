import random
import os
import time
print("Welcome to snake water gun game!!!")
tim = time.strftime("%H : %M : %S", time.localtime())
print("Current time is: ", tim)
pchoice = input("Enter your choice(snake,water or gun): ")
cchoice = random.choice(['snake','water','gun'])


if pchoice == cchoice:
    print("It's a Draw!!")


elif pchoice == 'snake' and cchoice == 'water':
    print("Snake drinks water!! You win!!")
elif pchoice == 'snake' and cchoice == 'gun':
    print("Gun shoots snake!! Computer wins!!")
elif pchoice == 'water' and cchoice =='gun':
    print("Gun can't shoot water!! You win!!")
elif pchoice == 'water' and cchoice == 'snake':
    print("Snake drinks water!! Computer wins!!")
elif pchoice == 'gun' and cchoice == 'snake':
    print("Gun shoots snake!! You win!!")
elif pchoice == 'gun' and cchoice == 'water':
    print("Gun can't shoot water!! Computer wins!!")

else:
    print("Invalid input!!")