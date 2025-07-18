#The format Built-in and str.format

pantry=[("veggies",10000.756734),("fruits",54574567.232)]
for i,item in enumerate(pantry):
    print("#",i+1,format(item[0].title(),"^10s"),"=",format(item[1],",.2f"))

pantry=[("veggies",10000.756734),("fruits",54574567.232)]
for i,item in enumerate(pantry):
    print("{}.{:<10}={:.2f}".format(i+1,item[0].title(),item[1]))

pantry=[("veggies",10000.756734),("fruits",54574567.232)]
for i,item in enumerate(pantry):
    print("#%(count)d %(item)-10s = %(price).2f %%"%{"count":i+1,"item":item[0].title(),"price":round(item[1])})
    print("{{}} {}.{:<10}={:.2f} {{}}".format(i+1,item[0].title(),item[1]))

pantry=[("veggies",10000.756734),("fruits",54574567.232)]
for i,item in enumerate(pantry):
    print("{{}} {0}.{1:<10}= {2:.2f} {{}}".format(i+1,item[0].title(),item[1]))

#Interpolated Format Strings

pantry=[("veggies",10000.756734),("fruits",54574567.232)]
for i,item in enumerate(pantry):
    print(f'{i+1}) \'{item[0].title()!r:^10}\' = {item[1]:.3f}')