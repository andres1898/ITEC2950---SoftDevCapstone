# datatime package that contain date, time and datetime
# date info is storage as number

from datetime import datetime, date, time

# current date
today = date.today()
print(today)

# specific date using int
tomorrow = date(2020, 8, 19)
print(tomorrow)

# specific date using str
next_week = date.fromisoformat('2020-8-19')
print(next_week)

# date + time
rigth_now = datatime.now()
print(right_now)
print(right_now.timestamp() # time stamp, express in seconds, not very human readable

# transform a timestamp to a date object
my_date = datetime.fromtimestamp(15000000)
print(my_date)

### TUPLES
# like a dictionary but can not be modified
city_state = [('Seattle', 'WA'),('Portland', 'OR'),('San Francisco', 'CA')]
# you can extract elements
first_city_state = city_state[0]
print(first_city_state)
# now you can call each part of the object
print(first_city_state[0])
print(first_city_state[1])
# unpack the elements into objects
city, state = first_city_state
print(city)
print(state)

# get distance in two measurments
def get_distance():
  miles = 1000
  km = miles * 1.6
  return miles, km # this will be return as a tuple

distance = get_distance() # tuple
print(distance[0])
print(distance[1])

miles, km = get_distance() # unpacked tuple
print(miles)
print(km)
