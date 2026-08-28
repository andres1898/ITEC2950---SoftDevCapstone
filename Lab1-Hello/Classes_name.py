# Todo create a program that ask the user to list the classes they are taking this semester

# empty list
classes_list = []

## Option 1, loop
while True:
    class_name = input("What classes are you taking this semester? click enter to end ")
    if not class_name:
        break
    classes_list.append(class_name)

# Option 2, braking into pieces
class_names = input("Enter your classes split by a commas: ")
list_of_classes = class_names.split(",") # split() to separate a string giving a character

for index, name in enumerate(list_of_classes): #enumerate() allows to loop through, while tracking of the index
    name_without_space = name.strip() #strip() deletes empty spaces before and after the string
    list_of_classes[index] = name_without_space

# print statement
for class_name in classes_list:
    print(class_name)
