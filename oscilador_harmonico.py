from vpython import *

"""GEOVANI LOPES SAMPAIO"""

cena = canvas(width='400', height='400')

ang = 0
A = 10
w = 1

pxi1 = A*cos(radians(ang))
pyi1 = A*sin(radians(ang))

pxi2 = A*cos(radians(ang))

pyi3 = A*sin(radians(ang))

p1 = sphere(pos=vector(pxi1,pyi1,0), radius=0.3, make_trail=True, trail_radius='0.05', color=color.blue)
p2 = sphere(pos=vector(pxi2,0,0), radius=0.3, make_trail=True, trail_radius='0.05')
p3 = sphere(pos=vector(0,pyi3,0), radius=0.3, make_trail=True, trail_radius='0.05')



t = 0
dt = 0.01

while True:
    rate(50)
    
    p1.pos = vector(A*cos(radians(ang)+w*t), A*sin(radians(ang)+w*t), 0)  
    p2.pos = vector(A*cos(radians(ang)+w*t), 0, 0)
    p3.pos = vector(0,A*sin(radians(ang)+w*t),0)
    
    t = t + dt
