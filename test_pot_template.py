import turtle
import math

window = turtle.Screen()
window.bgcolor("white")

def setup_template(new_turtle, angle):
	new_turtle.pendown()
	new_turtle.left((angle+45))

def draw_lobe(new_turtle, angle, side, top):
    new_turtle.forward(side)
    new_turtle.right((angle +45))
    new_turtle.forward(top)
    new_turtle.right((angle +45))
    new_turtle.forward(side)


def main():
	t = turtle.Turtle()

	t.shape("classic")
	t.color("red")
	t.penup()
	
	number_of_lobes = 5
	# this factor makes the template vertical vs. slanted
	angle = 360 + (360/number_of_lobes)
	side = 30
	top = 50

	setup_template(t, angle)

	for i in range(0,number_of_lobes):
		draw_lobe(t, angle, side, top)
		t.left(angle + 90)

	window.exitonclick()




if __name__ == '__main__':
	main()