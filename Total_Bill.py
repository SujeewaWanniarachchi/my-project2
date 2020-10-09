
Units=int(input("Enter Units:"))
if Units<=50:
     total=Units*5
elif Units<=150:
    total=(50*5)+((Units-50)*7)
elif Units<=200:
    total=50*5+100*7+((Units-150)*10)
else:
    total=50*5+100*7+100*10+((Units-200)*15)

print ("Total Bill:","Rs",total+(total*0.2))    
    
