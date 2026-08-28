# classes registered by a student
classes_registered = ['ITEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATH 1100']

# Make a list of only ITEC courses
only_itec = [ c for c in classes_registered if c.startswith('ITEC') ]
# list comprenhesion is list expression that implicate a loop and can have conditions and operations
only_itec = [ c for c in classes_registered if c.startswith('ITEC') ] # condition
code_lowcase = [ c.lower() for c in classes_registered] # operation, turn all the letter in lowercase

# Record temp every day. Record -1 if not possible to take measurements
hightemps = [-1, 78, 72, 67, -1, 51, 87, -1, 54, 67, 78, -1, 70]

#Make a list of only numbers that reoresent a valid temperature measurement
only_real_meas = [ temp for temp in hightemps if temp != -1 ] # filter 
print(only_real_meas)

temp_celcius = [ (temp_f - 32) * 5 / 9 for temp_f in only_real_meas] # operation, convert the result elements
print(temp_celcius)
