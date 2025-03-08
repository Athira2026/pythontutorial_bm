a=float(input())
b=float(input())
c=float(input())

if a+b>c and b+c>a and a+c>b:
   
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5            

    print("The area of the triangle is: {:.2f}".format(area))
else:
    print("Invalid Triangle")
