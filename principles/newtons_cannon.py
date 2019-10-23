from vpython import *

#######################################################

speed = -7800  # this is the useful variable to adjust; 8000 does a good orbit
angle = 90    # degrees up from positive x-axis

#######################################################

Earthradius = 6371000
initialpos = Earthradius*1.05*vector(cos(angle/180*pi),sin(angle/180*pi),0)
ballrad = 0.02*Earthradius

scene = canvas(width=1050, height=750, x=0, y=0, background=color.white, fov=0.001, range=2*Earthradius)

Earth = sphere(pos=vector(0,0,0), radius=Earthradius, color=color.green, opacity=0.2)

# initialize the cannonball coming out of Newton's cannon
NewtonCannon = sphere(pos=vector(initialpos), radius=ballrad, color=color.blue)
NewtonCannon.velocity = speed * vector(initialpos.y,-initialpos.x,initialpos.z)/mag(initialpos)
NewtonCannon.acceleration = - 9.8 * NewtonCannon.pos / mag(NewtonCannon.pos)  #make point to center of Earth always
NewtonCannon.trail = curve(color=NewtonCannon.color)   #trace path

# initialize the cannonball dropped through the center of the Earth
droppedUniform = sphere(pos=vector(initialpos), velocity=vector(0,0,0), radius=ballrad, color=color.red)
droppedUniform.acceleration = -9.8 * droppedUniform.pos / mag(droppedUniform.pos)
droppedUniform.trail = curve(color=droppedUniform.color)

# initialize the cannonball dropped toward an Earth-equivalent point mass at Earth's center
droppedCentral = sphere(pos=vector(initialpos), velocity=vector(0,0,0), radius=ballrad, color=vector(0.7,0.7,0.7))
droppedCentral.acceleration = -9.8 * droppedCentral.pos / mag(droppedCentral.pos)
droppedCentral.trail = curve(color=droppedCentral.color)

t = .1				# set the time step
t_elapsed = 0		# we want to keep track of elapsed time, so zero the variable now

#scene.mouse.getclick()          # don't start until we click


while ( mag(NewtonCannon.pos) >= Earthradius):
    rate(4000)
 
    NewtonCannon.pos = NewtonCannon.pos + NewtonCannon.velocity*t + 0.5*NewtonCannon.acceleration*t**2
    NewtonCannon.trail.append(pos=NewtonCannon.pos)
    NewtonCannon.velocity = NewtonCannon.velocity + NewtonCannon.acceleration*t
    NewtonCannon.acceleration = - 9.8 * NewtonCannon.pos / mag(NewtonCannon.pos)
    
    droppedUniform.pos = droppedUniform.pos + droppedUniform.velocity*t + 0.5*droppedUniform.acceleration*t**2
    droppedUniform.trail.append(pos=droppedUniform.pos)
    droppedUniform.velocity = droppedUniform.velocity + droppedUniform.acceleration*t
    droppedUniform.acceleration = - 9.8 * (min( mag(droppedUniform.pos),Earthradius )/Earthradius)**3 * droppedUniform.pos / mag(droppedUniform.pos)
    # Cubed term scales gravity by mass enclosed (Gauss' law) assuming constant density Earth (which is false).    
    
    droppedCentral.pos = droppedCentral.pos + droppedCentral.velocity*t + 0.5*droppedCentral.acceleration*t**2
    droppedCentral.trail.append(pos=droppedCentral.pos)
    droppedCentral.velocity = droppedCentral.velocity + droppedCentral.acceleration*t
    droppedCentral.acceleration = - 9.8 * droppedCentral.pos / mag(droppedCentral.pos)
    # This version treats all Earth's mass as being at Earth's center.  
    
    t_elapsed = t_elapsed + t
    
totaltime = t_elapsed/60 
label(pos=(Earthradius*1.1,Earthradius*1.1,0), text='elapsed time = %1.3f minutes' % totaltime)    

# Written by Lenore Horner SIUE October 22, 2009.
# Version 2 - March 26, 2010: real radius, can start from arbitrary position, show time to crash in 
### display window