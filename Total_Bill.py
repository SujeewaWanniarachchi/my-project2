
units=int(input("Enter Units:"))
if units<=50:
     total=units*5
elif units<=150:
    total=(50*5)+((units-50)*7)
elif units<=200:
    total=50*5+100*7+((units-150)*10)
else:
    total=50*5+100*7+100*10+((units-200)*15)

print ("Total Bill:","Rs",total+(total*0.2))    
    
