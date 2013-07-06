balance = 320000
annualInterestRate = 0.20

testbalance = balance
monthlyInterestRate = annualInterestRate / 12
low = balance / 12.0
high = (balance*(1 + monthlyInterestRate)**12)/12.0
epsilon = 0.01
min_payment = (high + low)/2.0

while abs(testbalance) >= epsilon:
    testbalance = balance
    for month in range(1, 13):
        testbalance = (testbalance - min_payment) * (1 + monthlyInterestRate)
    if testbalance >= 0.0:
       low = min_payment
    elif testbalance <= 0.0:
        high = min_payment
    min_payment = (high + low)/2.0
print 'lowest payment: ',round(min_payment,2)
