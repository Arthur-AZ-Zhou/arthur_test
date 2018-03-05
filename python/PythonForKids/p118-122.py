#The Len function
len('This is a test string')
creature_list = ['unicorn','cyclops','fairy','elf','dragon','troll']
print(len(creature_list))
fruit = ['apple','banana','clementine','dragon fruit']
length = len(fruit)
for x in range(0,length):
    print('The fruit at index %s is %s' % (x,fruit[x]))
#Max and Min Functions
numbers = [5,4,10,30,22]
print(max(numbers))
strings = 's,t,r,i,n,g,S,T,R,I,N,G'
print(max(strings))
guess_this_number = 61
player_guesses = [12,15,17,45]
if max(player_guesses)> guess_this_number:
    print('Boom! You all lose!')
else:
    print('You win')
#The range function
for x in range(0,10):
    print (x)
print(list(range(0,5)))
#The sum function
mylist = list(range(0,500,50))
print(mylist)
print(sum(mylist))
