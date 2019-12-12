# Write a program to calculate the nth Fibonacci number.

def main():
    last = int(input("Which fibonacci number do you need? "))
    numbers = [1, 1]

    for i in range(1, last - 1):
        next = numbers[i] + numbers[i-1]
        numbers.append(next)

    print("The nth Fibonacci number is",numbers[last - 1])
    
main()
