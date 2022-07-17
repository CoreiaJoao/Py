print("Welcome to the tip calculator.")
(price_bill)=float(input("What wat the total bill? $"))
total_people=int(input("How many people to split the bill? "))
percentage=float(input("What percentage tip would you like to give? 10, 12 or 15? "))/100
each_person_pay = round((((price_bill)/total_people) +  ((price_bill)/(total_people))*percentage),2)
result= str(each_person_pay)
print(f"Each person should pay: ${result}")