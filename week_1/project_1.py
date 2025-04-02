# Python program to find the Simple Interest
# Compond interest 
# Annuity Plan



Principal = float(input("What is the Principal?:"))
Rate = float(input('What is the rate?:'))
Time = float(input('What is the time?:'))
Number_of_times_interest_is_compounded = float(input("What is the Number of times interest is compounded?:"))
Periodic_payment = float(input("What is the periodic payment?:"))

str1 =("The Simple Interest is!")
print(str1)  

Amount1 = Principal * (1 + ((Rate / 100) * Time) )
print(Amount1)

str2 =("The Compound Interest is!")
print(str2)

Amount2 = Principal * (1 + (Rate / Number_of_times_interest_is_compounded)**Number_of_times_interest_is_compounded * Time)
print(Amount2)

str3 =("The Annuity Plan is!")
print(str3)

Amount3 = Periodic_payment * (((1 + (Rate / Time)) ** (Number_of_times_interest_is_compounded * Time) - 1) / (Rate / Number_of_times_interest_is_compounded))
print(Amount3)