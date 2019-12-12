# Write definitions for the following 2 functions:
#   1. sumN(n) returns the sum of the first n natural numbers
#   2. sumNcubes(n) returns the sum of the cubes of the first n natural numbers

# Then use these functions in a program that prompts a user for an n and prints out the sum 
# of the first n natural numbers and the sum of the cubes of the first n natural numbers.

def sumN(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("The sum from 1 to",n ,"is", total)

def sumNcubes(n):
    cubesTotal = 0
    for i in range(1, n + 1):
        cubesTotal += i ** 3
    print("the sum of 1 to", n, "cubes is", cubesTotal)

def main():
    n = int(input("Enter a number: "))
    sumN(n)
    sumNcubes(n)

main()





