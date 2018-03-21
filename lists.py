
my_list = [0, 1, 2, 3, 4, 5]
print(my_list)
print(my_list[3])
print(my_list[-1])
print(my_list[3:])
print(my_list[:2])
print(my_list[0::1])
print(my_list[0:-1:1])
print(my_list[0::2])
print(my_list[::2])
my_list[-1]="a"
print(my_list)
my_list[-1]=5
my_list.append(6)
print(my_list)
my_list += [7, 8, 9]
print(my_list)
my_list[1:3] = ['b', 'c']
print(my_list)
my_list[0] = 'a'
my_list[3:] = []
print(my_list)
my_list[-1:] = ['d', 'a']
print(my_list)
my_list.remove('a')
print(my_list)
print(my_list.pop())
print(my_list.pop(-1))
print(my_list)

