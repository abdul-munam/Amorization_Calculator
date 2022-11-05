j=1
n=12
P=float(input("Enter principal amount : "))
t=float(input("Enter time in terms of years : "))
r=float(input("Enter interest rate : "))/100

monthly_payment=round((r*P)/(n*(1-((1+(r/n))**((-n)*t)))),2)
total_interest=round((n*monthly_payment*t)-P,2)
monthly_rate=r/n

print("\nMonthly Payment : ",monthly_payment)
print("Total Payment : ",P+total_interest,"\n")

print("Month\tBeginning Balance\tInterest\tPrincipal\tEnding Balance")
for i in range(int(n*t)):
    print(i+1,end="\t")
    if i==0:
        print(str(P),end="\t\t")
    elif i>0:
        print(str(ending_balance),end="\t\t")
    interest_payment=round(P*monthly_rate,2)
    print(str(interest_payment),end="\t\t")
    principal_payment=round(monthly_payment-interest_payment,2)
    print(str(principal_payment),end="\t\t")
    ending_balance=round(P-principal_payment,2)
    print(str(ending_balance))
    P=round(P-principal_payment,2)
    if ((i+1)%12)==0:
        print(f"----------------------------------Year {j} End--------------------------------\n")
        j+=1
print("Total interest paid : ",total_interest,"\n")