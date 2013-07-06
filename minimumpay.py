balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
paid = 0
month = 1

for month in range (1,13):
    minimumpay = monthlyPaymentRate * balance
    balance = (balance - minimumpay) * (1 + annualInterestRate / 12)
    print 'Month: ', month
    print 'Minimum monthly payment: ', round(minimumpay,2)
    print 'Remaning Balance: ', round(balance,2)
    paid = paid + minimumpay

print 'Total Paid: ', round(paid,2)
print 'Remaining Balance: ', round(balance,2)
    
    




