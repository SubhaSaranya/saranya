dic={1:400,2:750,10:3250,50:1500}
n=int(input())
s=0
if (n>=50):
    s+=(n//50)*dic[50]
    n=n%50
if (n>=10):
    s+=(n//10)*dic[10]
    n=n%10
if (n>=2):
    s+=(n//2)*dic[2]
    n=n%2
if (n>=1):
    s+=(n//1)*dic[1]
    n=n%1   
print(s)
