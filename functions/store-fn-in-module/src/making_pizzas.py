import pizza
from pizza import make_pizza
from pizza import make_pizza as mp
import pizza as p

# import all functions
from pizza import *

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza(16, 'pepperoni')

mp(16, 'pepperoni')

p.make_pizza(16, 'pepperoni')