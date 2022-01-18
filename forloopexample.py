"""
for loop
==========
for item in collection :
    statements
"""

nums=[0,1,2,3,4]
print(nums)

x=list(range(5))
print(x)

y=list(range(20,31))
print(y)

z=list(range(20,31,3))
print(z)

p=list(range(50,0,-1))
print(p)

for q in range(10):
    print(q,end='\t')

for s in range(1,10):
    print(s,end='\t')

for a in range(50,101,5):
    print(a,end='\t')

sum=0
for n in range(1,11) :
    sum=sum+n

print(sum)


sum=0
for n in range(1,11) :
    sum=sum+n**2

print(sum)


sum=0
for n in range(1,11) :
    sum=sum+n
    print(n,end='+')

print(chr(8)+'='+str(sum))


# c=input('enter a character :')
# print(f'the ASCII value of {c} is {ord(c)}')

# i=int(input('enter a ASCII value :'))
# print(f'the character of {i} ASCII value is {chr(i)}')



for n in range(65,91) :
     print(chr(n),end='\t')

print('\n')

for n in range(97,123) :
     print(chr(n),end='\t')


mylist=[2,5,8,1,3]
for a in mylist :
    print(a, end='\t')

print('\nmaximum =',max(mylist))
print('\nminimum =',min(mylist))

import time
s='My name is Sunny Deol urofe Moshiur Rahman'
for c in s :
    print(c, end=' ',flush=True)
    time.sleep(.1)


fact=1
num=int(input('please enter a number :'))
if num>=0:
    for x in range(1,num+1) :
        fact=fact*x
        
    print(f'the factorial of {num} is :{fact}')
else:
    print('Sorry, the number is -ve. Please try again later.')


for num in range(1,101):
    prime=True
    # num=8
    for x in range(2,num) :
        if num%x==0:
            prime=False
            break

    # if prime:
    #     print('the number is prime')
    # else :
    #     print('the number is not prime')

    if prime :
        print(num, end='\t')
