# Exchange first and second/last index value of color.

color = [ 'red', 'green', 'blue', 'yellow', 'orange']

print(id(color))
print(type(color))
print('value of original list :',color)

temp = color[0]   # value change

print('value of zero index value:',color[0])
print('value of last index value:',color[-1])

color[0] = color[-1]        

print('changed zero index value:', color[0])
print('change update list of value:',color)

# exchange first and second index value .
color[-1] = temp
print('list values first and last index:', color)

