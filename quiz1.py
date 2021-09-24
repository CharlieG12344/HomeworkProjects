#Ask user for two numbers
num1 = input("Choose the first number ")
num2 = input("Choose the second number ")
# Create a loop that does the following until the product and sum are the same
sum = int(num1) + int(num2)
prod = int(num1) * int(num2)
# Calculate and disply their sum
while (sum != prod):
    print("Your sum is " + str(sum))
    print("Your product is " + str(prod))
    print("Your sum and product are not equal")
    num1 = input("Choose a new number ")
    num2 = input("Choose a second new number ")
    sum = int(num1) + int(num2)
    prod = int(num1) * int(num2)
print("Your sum and product are equal!")

# Calculate and display their product


# If their sum and their product are equal - tell the user
# otherwise ask for two more numbers