balance = 3926
annualInterestRate = 0.2
payment = 10

def payoff(payment,balance):
    for month in range(1,12):
        balance = (balance - payment) * (1 + annualInterestRate / 12)
    return balance


for payment in range(10,balance,10):
    if payoff(payment,balance) <= 0:
        break

print 'Lowest Paymnet: ',payment
    




