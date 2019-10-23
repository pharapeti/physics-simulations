from vpython import *

ball = sphere(pos=vector(-3,10,0), radius=0.5, color=color.cyan, make_trail=True)
ball.trail = curve(color=ball.color)

wallL = box(pos=vector(-4,0,0), size=vector(0.1,16,16), color=color.green)
wallR = box(pos=vector(4,0,0), size=vector(0.1,16,16), color=color.green)

ball.velocity = vector(40,0,0)

vscale = 0.05
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.yellow)

deltat = 0.005
t = 0

scene.autoscale = False

def createImpactPoint():
	return arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.red)

while t < 3:
	rate(100)
	if ball.pos.x < wallL.pos.x and ball.pos.y < wallL.size.y/2:
		ball.velocity.x = -ball.velocity.x
		createImpactPoint()
	if ball.pos.x > wallR.pos.x and ball.pos.y < wallR.size.y/2:
		ball.velocity.x = -ball.velocity.x
		createImpactPoint()

	ball.pos = ball.pos + ball.velocity*deltat
	ball.velocity.y -= 0.8
	t+= deltat