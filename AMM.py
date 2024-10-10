

const = 485*267600
prise_token_1 = 8.8
prise_token_2 = 0.041

a1=100000
b1=2
a=1

while a1-b1 >5 or a1-b1 <-5:
    b=const/a
    a1=a*prise_token_1
    b1=b*prise_token_2
    a+=0.001

print (f"token A is  {a}")
print (f"token B is  {b}")

