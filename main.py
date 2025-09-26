# date time module

import datetime

x = datetime.datetime.now()

print(x)

# the above program made it so that i can see the current time using the datetime.datetime.now() module.

py = dir(datetime)

print(py)

#  using the dir function I can see all the functions within a module.

import math

s = math.sqrt(74646.99984534)
dy = dir(math)

print(s)
print(dy)

# the above module helped me get the squareroot of any number i desired.

import datetime as d

f = d.datetime.now()

print(f)

# the above program was the same as the first but with a minor difference being that the module name was shortened down to "d".

h = d.date.today()

print(h)