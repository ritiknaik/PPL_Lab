x=10
y=20
c=x*(y-x)-1
if c>100:
    raise Exception("Number is greater than 100")
else:
    print(c)