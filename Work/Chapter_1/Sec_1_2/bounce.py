# bounce.py
#
# Exercise 1.5

init_height = 100.0 # in meters
interim_height = init_height

for i in range(10):
    bounce_height = (3/5) * interim_height
    print(i, round(bounce_height, ndigits=4))
    interim_height = bounce_height