# Write and test a function to meet this specification:

# squareEach(nums) 
# nums is a list of numbers. 
# Modifies the list by squaring each entry.

def squareEach(nums):
    squares = []
    for n in nums:
        squares.append(n ** 2)
    print(squares)


def main():

    nums = [1, 3, 5, 7, 9]
    
    squareEach(nums)

main()
