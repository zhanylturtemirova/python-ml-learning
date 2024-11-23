#list
mixed_list = ["asd", 11, 34, ["er", 23], 1.2, 4]
mixed_list.append(3)
print(mixed_list)
copy_mixed_list = mixed_list.copy()
print(copy_mixed_list)
# copy_mixed_list.clear()
mixed_list.extend([3,4,5])
print(mixed_list)
mixed_list.insert(1, "ttt")
print(mixed_list)
mixed_list.remove(34)
print(mixed_list)
mixed_list.reverse()
print(mixed_list)
print(copy_mixed_list)
print(mixed_list)
mixed_list.pop()
mixed_list.append("???")
print(mixed_list)
print(mixed_list.count(4))


#tuple

tuple1= ("A","F","S","C")
print(tuple1.count("A"))
print(tuple1.index("A"))

#set
arr1 = [10,2,2,1,10, 2]
set1 = set(arr1)
print(set1)
set1.remove(2)
print(set1)
set1.add("FFFF")
print(set1)
set1.pop()
print(set1)

#dictionary

my_dict = {'name': 'QWERTY', 'age':  90, 'title': 'example'}
print(my_dict.get('name'))
print(my_dict.get('job'))
print(list(my_dict.items())[1][0])
print(list(my_dict.items())[1][1])
print(list(my_dict.keys()))
print(list(my_dict.values()))
my_dict2 = {'name': 'NEW QWERTY', 'age':  99, 'title': 'NEW example'}
my_dict.update(my_dict2)
print(my_dict)
my_dict.pop('title')
print(my_dict)
my_dict.popitem()
print(my_dict)
for key, value in my_dict.items():
    print(key, value)