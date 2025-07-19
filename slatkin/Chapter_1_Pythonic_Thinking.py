# Item 4: Prefer Interpolated F-Strings

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

pantry=[("veggies",10000.756734),("fruits",54574567.232)]
for i,item in enumerate(pantry):
    print(f'{i+1}) \'{item[0].title()!r:^10}\' = {item[1]:.3f}')

# Item 6: Prefer Multiple Assignment Unpacking Over Indexing

cars={'toyota':1900,'bmw':2000,'aston_martin':2004,'porsche':2006}
items=tuple(cars.items())
for item in items:
    print(item[0],'=',item[1]) # indexing
    car,year=item # use unpacking instead of indexing
    print(car,'=',year)

cars={'toyota':('land_cruser',1900),'bmw':('m4',2000),'aston_martin':('vanquish',2004),'porsche':('911_GT3_RS',2006)}
items=tuple(cars.items())
for item in items:
    brand,(model,year)=item # unpacking for multiple assignments
    print(brand,model,'=',year)

def bubble_sort(seq):
    for _ in range(len(seq)):
        for i in range(1,len(seq)):
            if seq[i]<seq[i-1]:
                seq[i-1],seq[i]=seq[i],seq[i-1]
    return seq

cars={'toyota':1900,'bmw':2000,'aston_martin':2004,'porsche':2006}
items=list(cars.keys())
print(bubble_sort(items))

cars={'toyota':1900,'bmw':2000,'aston_martin':2004,'porsche':2006}
items=tuple(cars.items())
for i in range(len(items)):
    print(f'#{i+1} {items[i][0]} = {items[i][1]}')# indexing
for rank,(brand,year) in enumerate(items,1): # use enumerate instead of indexing
    print(f'#{rank} {brand} = {year}')