print("Welcome to the Tip Calculator!\n")
bill=float(input(("What was the total bill?\nTk ")))
tip=int(input("How much tip would you like to give? 5, 10 or 12\n")) #tips is in percentage
how_many=int(input("How many people to split the bill?\n"))
ntip=(tip/100)*bill #ntip is total tip
fbill=bill+ntip #fbill is final bill amount bill+tip
pay=(fbill/how_many) #per person shoul pay
'''fpay=round(pay,2) ''' #there is formating error in round function so we will use format function 
fpay="{:.2f}".format(pay)#format function
print(f"Each person should pay:Tk {fpay}") #result in 2 decimal places