pocketMoney = 0.01
totalMoney = 0 # TASK 3

for week in range(1,27): # TASK 1 - remember to go 1 number higher
    print("\nIt is week",week)
    print("You will get £",pocketMoney)
    totalMoney = totalMoney + pocketMoney # TASK 3
                                          # Must be done before doubling
                                          # the pocketMoney for next week
    pocketMoney = pocketMoney * 2 # TASK 2
    
print("\n\nTotal pocketMoney to date £",totalMoney) # TASK 3
                                               # Must be done after the loop
                                               # (not indented)

input("\nPress ENTER to exit program")


# TASK 1
# Change the loop so that it counts which week it is (from 1 to 26)

# TASK 2
# Inside the loop set the pocketMoney value to 2x what it was
# Hint: pocketMoney = .........

# TASK 3
# Add another variable called totalMoney at the start of the program
# totalMoney = 0

# Inside the loop keep a running total of your pocketMoney so far
# Only print the total amount at the END of the program (outside the loop)

