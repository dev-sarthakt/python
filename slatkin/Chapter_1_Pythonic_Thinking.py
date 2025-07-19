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
    
# Item 8: Use zip to Process Iterators in Parallel

cars=['toyota','bmw','aston_martin','porsche']

counts=list(len(n) for n in cars) # list comprehensions
print(counts)

longest_name=None
max_count=0
for i in range(len(cars)):
    count=counts[i]
    if count>max_count:
        max_count,longest_name=count,cars[i]
print(longest_name)

longest_name=None
max_count=0
for i,name in enumerate(cars):
    count=counts[i]
    if count>max_count:
        max_count,longest_name=count,cars[i]
print(longest_name)

longest_name=None
max_count=0
for car,count in zip(cars,counts):
    if count>max_count:
        max_count,longest_name=count,car
print(longest_name)

import itertools
longest_name=None
max_count=0
cars.append('ferrari')
for car,count in itertools.zip_longest(cars,counts):
    print(car,count)

# Item 9: Avoid else Blocks After for and while Loops

for i in range(3):
    print(i)
else: # else block runs
    print('for block compleated')
for i in range(3):
    if i == 2:
        break
    else:
        print(i)
else: # else block dosen't run
    print('for block incompleated cause of break')

for x in []:
    print('This is skipped for empty list')
else:
    print('directly prints this')

while False:
    print('This is skipped')
else:
    print('directly prints this')

def coprime(a,b):
    for i in range(2,min(a,b)+1):
        if a%i==0 and b%i==0:
            print('Not coprime')
            break
    else:
        print('Coprime')
coprime(3,11)

# Item 10: Prevent Repetition with Assignment Expressions

def lemonade(count):
    print(count,'lemons squeezed')

fresh_fruit = {
'apple': 10,
'banana': 8,
'lemon': 5,
}

count=fresh_fruit.get('lemon',0) # here 0 is the default value in case lemon dosent exist
if count:
    lemonade(count)

if count:=fresh_fruit.get('lemon',0): # walrus operator
    lemonade(count)

count=fresh_fruit.get('lemon',0)
if count>=4:
    lemonade(count)

if (count:=fresh_fruit.get('lemon',0))>=4:
    lemonade(count)

fruits=list(fruit for fruit,_ in fresh_fruit.items())
fruits.extend(['mango', 'dragonfruit'])
print(fruits)
fruits.append(['grapes','strawberry'])
print(fruits)
