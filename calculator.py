# A very basic calculator program that allows for addition, subtraction, 
# multiplication and divison.

# An opening description of how to use different operations in the calculator.
print("Please choose operation from the following choices: ")
print("Enter 1 for addition.")
print("Enter 2 for subtraction.")
print("Enter 3 for multiplication.")
print("Enter 4 for division.")

# Where the user chooses an int between 1 and 4 for which operation they want
choice = input("Enter operation number: \n")

# If statement that handles addition.
if choice == '1':
    num_1 = float(input("Enter first number to add: "))
    num_2 = float(input("Enter second number to add: "))
    result = float(num_1 + num_2)
    print(str(result))

# If statement that handles subtraction.
if choice == '2':
    num_1 = float(input("Enter first number to subtract from: "))
    num_2 = float(input("Enter number to subtract: "))
    result = float(num_1 - num_2)
    print(str(result))

# If statement that handles multiplication
if choice == '3':
    num_1 = float(input("Enter a number to multiply: "))
    num_2 = float(input("Enter a number to multiply by: "))
    result = float(num_1 * num_2)
    print(str(result))

# If statement that handles division
if choice == '4':
    num_1 = float(input("Enter a number to divide: "))
    num_2 = float(input("Enter a number to divide by: "))
    result = float(num_1 / num_2)
    print(str(result))

