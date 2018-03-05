#Randit
import random
print(random.randint(1,100))
print(random.randint(100,1000))
print(random.randint(1000,10000))
import random
num = random.randint(1,100)
x = 0
while True:
    guess = input("Guess a number between 1 and 100 ")
    if int(guess) == num:
        x = x+1
        print("You have AMAZING guessing skillz. It took you", x, "guesses to guess the number!")
    elif int(guess) < num:
        print("Try higher ")
        x = x + 1
    elif int(guess) > num:
        print("Try lower ")
        x = x+1
#Dessert list
import random
desserts = ['ice cream', 'pancakes','brownies', 'cookies', 'candy']
print(random.choice(desserts))
# shuffle
import random
desserts = ['ice cream', 'pancakes','brownies', 'cookies', 'candy']
random.shuffle(desserts)
print(desserts)
# sys
import sys
sys.exit()
#read w/ stdin
import sys
v = sys.stdin.readline()
I ran away from the wolf but I ran into a bear.
print (v)
v = sys.stdin.readline(13)
I ran away from the wolf but I ran into a bear.
print(v)
