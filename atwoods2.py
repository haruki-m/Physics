from visual import *
scene.center=(0,5,0)
floor=box(pos=(0,-0.5,0),size=(16,1,12),color=color.white)

mass1=box(pos=(-4,5,0),length=1,height=2,width=2,color=color.red)
pt1=mass1.pos+vector(0,mass1.height/2,0)
mass1.vel=vector(0,0,0)

mass2=box(pos=(+4,5,0),length=1,height=2,width=2,color=color.blue)
pt2=mass2.pos+vector(0,mass2.height/2,0)
mass2.vel=vector(0,0,0)

pulley=cylinder(pos=(0,15,-.5),radius=4,axis=(0,0,1),color=color.yellow)
rope=curve(pos=[pt1,(-4,15,0),(4,15,0),pt2])

mass1.mass=float(input("Red mass(kg):"))
mass2.mass=float(input("Blue mass(kg):"))
print ("\n")

t=0
dt=0.001
g=vector(0,-9.8,0)
mass2.acc=(mass2.mass-mass1.mass)/(mass1.mass+mass2.mass)*g
mass1.acc=-mass2.acc

while mass2.pos.y-1 > 0 and mass1.pos.y-1 > 0:
    rate(400)
    
    for obj in (mass1,mass2):
        obj.vel = obj.vel + obj.acc*dt
        obj.pos = obj.pos + obj.vel*dt

    rope.pos[0]=mass1.pos+vector(0,mass1.height/2,0)
    rope.pos[3]=mass2.pos+vector(0,mass2.height/2,0)
    
    t=t+dt

print ("Heavy mass hits floor")
print ("Time (s): %.2f" % (t))
print ("Velocity up (m): %.2f" % (mass1.vel.mag))
print ("----------")

for obj in (mass1,mass2):
    if obj.vel.y>0:
        obj.Up=True
    else:
        obj.Up=False

while (mass1.Up and mass1.vel.y>0) or (mass2.Up and mass2.vel.y>0):
    rate(400)

    for obj in (mass1,mass2):
        if obj.Up:
            obj.vel = obj.vel + g*dt
            obj.pos = obj.pos + obj.vel*dt

    rope.pos[0]=mass1.pos+vector(0,mass1.height/2,0)
    rope.pos[3]=mass2.pos+vector(0,mass2.height/2,0)
    
    t=t+dt

print ("Max Height at:")
print ("Time (s): %.2f" % (t))
height=max(mass1.pos.y,mass2.pos.y)
print ("Height (m): %.2f" % (height))
