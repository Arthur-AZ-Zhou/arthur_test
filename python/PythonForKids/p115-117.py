#The Eval function
eval('10*40')
your_calculation = input('Enter a calculation:')
eval(your_calculation)
#The Exec function
my_small_program = '''print('ham')
print('sandwich')'''
exec(my_small_program)
#The float function
your_age = input('Enter ur age:')
age = float(your_age)
if age > 13:
    print("You are %s years too old" % (age - 13))
#The int function
int(123.456)
int('123')
# (Error) int('123.456')

    
