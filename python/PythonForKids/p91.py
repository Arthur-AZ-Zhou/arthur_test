
import sys

def moon_weight():
    print('Please enter your current Earth weight')
    weight = float(sys.stdin.readline())
    print('Please enter the amount your weight might increase each year')
    weight_increase=float(sys.stdin.readline())
    print('Please enter the number of years')
    years = float(sys.stdin.readline())
    weight = weight + weight_increase * years
    print("your weight after %s years: %s" %(years, weight))

moon_weight()

