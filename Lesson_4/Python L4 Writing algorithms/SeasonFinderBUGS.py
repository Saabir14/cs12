#Season finder with 3 bugs

#input the month of the year and the program 
#will tell you which season it is in

month = input("Enter the month of year: ")
month = Month.title()

if month == "December" or month = "January" or month == "February":
    print(month,"is in Winter")
elif month == "March" or month == "April" or month == "May":
    print(month,"is in Spring")
elif month == "June" or month == "July" or month == "August":
    print(month,"is in Summer")
elif month == "September" or month == "October" or month == "November":
    Print(month,"is in Autumn")
else:
    print("Check spelling of month.")
    
input("Press ENTER to quit")
