#coding=utf-8


colors = ['black','white']
sizes = ['S','M','L']
t_shirts = [(color,size) for color in colors for size in sizes]
print(t_shirts)

for color in colors:
    for size in sizes:
        print((color,size))

t_shirts_3 = [(color,size) for size in sizes for color in colors]
print(t_shirts_3)