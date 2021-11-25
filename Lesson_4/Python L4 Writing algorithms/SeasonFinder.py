#Season finder with 3 bugs

#input the month of the year and the program
#will tell you which season it is in

###"moth" of the year - spelling error in comment,not a bug
###since it will not affect the running of the program

month = input("Enter the month of year: )
###bug1: Missing "

#variable.title() converts to title case with capital first letter
month = month.title()

if month == "December" or month = "January" or month == "February": ###bug2: single '=' sign
    print(month,"is in Winter")
elif month == "March" or month == "April" or month == "May":
    print(month,"is in Spring")
elif month == "June" or month == "July" or month == "August":
    print(month,"is in Summer")
elif month == "September" or month == "October" or month == "November":
    Print(month,"is in Autumn") ###bug3: Print is capitalised
else:
    print("Check spelling of month.")
    
input("Press ENTER to quit")
