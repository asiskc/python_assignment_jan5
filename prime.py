P_list = list(range(0,100))
P_list=list(filter(lambda x:x%2!=0,P_list))
#4.filter prime numbers
fp = open("\home\Desktop\primes.txt","a")

for num in P_list:
    for i in range(2,num-1):
        if (num%i == 0):
            break
    else:
        fp.write("{}\t".format(str(num)))
fp.close()

#5.using context manager
with open("\home\Desktop\primes1.txt","a") as fp:
    for num in P_list:
        for i in range(2, num - 1):
            if (num % i == 0):
                break
        else:
            fp.write("{}\t".format(str(num)))

#6.read txt file created
with open("\home\Desktop\primes1.txt","r")as fp:
    print(fp.read())
