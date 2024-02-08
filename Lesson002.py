import turtle
num_circles = 36
radius = 100
angle = 10
animation_speed = 0

turtle.speed(animation_speed)

for x in range(num_circles):
    turtle.circle(radius)
    turtle.left(angle)

turtle.done()