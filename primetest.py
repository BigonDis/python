import math
odd = 3
prime = 0
count = 0
            
while count < 10:
    print odd;
    for x in range(2,odd):
        if odd%x == 0:
            print odd, "is not prime"
            break
    else:
        prime = odd
        print prime, "is a prime number"
        count = count + 1
    odd = odd + 2
    

    
    
        
