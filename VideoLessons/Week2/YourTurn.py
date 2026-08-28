### TODO Start with a list [2,4,6] and create a list comp to end up with [3,5,7]

initial_list = [2, 4, 6]
comp_list = [ num + 1 for num in initial_list ]
print(comp_list)

### TODO start with [0, 3, 4, 0, 22, 1], end with [3, 4, 22, 1]
initial_list = [0, 3, 4, 0, 22, 1]
comp_list = [ num for num in initial_list if num != 0]
print(comp_list)

### TODO start with ['ITEC 2560', 'BTEC 1010', 'ITEC 2905'] end with classes that are not ITEC
initial_list = ['ITEC 2560', 'BTEC 1010', 'ITEC 2905']
comp_list = [ course for course in initial_list if not course.startswith('ITEC') ]
print(comp_list)

### TODO start with [0, 10, 4, 0, 32], end with [20, 8, 64]
initial_list = [0, 10, 4, 0, 32]
comp_list = [ num * 2 for num in initial_list if num != 0]
print(comp_list)