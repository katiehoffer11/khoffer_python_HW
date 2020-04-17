# Initial variable to track game play
run = 'y'
  
# Set start and last number
first_number = 0


# While we are still playing...
while run == "y":
    
    # Ask the user how many numbers to loop through
    user_number = int(input("How many numbers? "))
    
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(first_number, (first_number + user_number)):
    
        # Print each number in the range
        print(x)
    # Set the next start number as the last number of the loop
    first_number = x + 1

    # Once complete... ask if the user wants to continue
    run = input("Would you like to continue:(y)es or (n)o? ")
