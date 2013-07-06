balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12
balance1 = balance
low = balance1/12
high =balance1*((1 + annualInterestRate)/12)
mid = (low + high) / 2
while (high - mid)> .01 or (mid - low) >.01:
    month = 1
    balance1 = balance
    while month <= 12:
        balance1 = round((balance1 - mid)*(1 + annualInterestRate/12),2)
        month = month + 1
    if balance1 < 0:
        high = mid
    else:
        low = mid
    mid = round((low + high)/2,2)
   
print("Lowest payment: " + str(mid))
