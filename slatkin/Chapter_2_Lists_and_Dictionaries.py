# Item 11: Know How to Slice Sequences

alphabets='qwertyuiopasdfghjklzxcvbnm'
alphabets_list=list(x for x in alphabets)
print(alphabets_list[1:25])

alphabets_list[-10:]=[i for i in range(10)]
print(alphabets_list)

# Item 12: Avoid Striding and Slicing in a Single Expression

odd=alphabets[::2]
print(odd)
even=alphabets[1::2]
print(even)

x=alphabets[-3::-2]
print(x)

# Item 13: Prefer Catch-All Unpacking Over Slicing

car_ages=[i for i in range(15)]
reverse_sorted_car_ages=sorted(car_ages,reverse=True)
# oldest,second_oldest=reverse_sorted_car_ages # Error
oldest,second_oldest,others=reverse_sorted_car_ages[0],reverse_sorted_car_ages[1],reverse_sorted_car_ages[2:] # Noob
print(oldest,second_oldest,others)
oldest,second_oldest,*others=reverse_sorted_car_ages # Pro
print(oldest,second_oldest,others)
oldest,*others,youngest=reverse_sorted_car_ages
print(oldest,others,youngest)
*others,second_youngest,youngest=reverse_sorted_car_ages
print(others,second_youngest,youngest)
# *others=reverse_sorted_car_ages # Error
# *first,*second,last=reverse_sorted_car_ages # Error
it=iter(range(10))
print(next(it))

# Item 14: Sort by Complex Criteria Using the key Parameter