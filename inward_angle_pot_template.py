from save_to_svg import saveImg
import turtle

window = turtle.Screen()
window.bgcolor("white")

def setup_template(new_turtle, angle):
	new_turtle.pendown()
	new_turtle.left(angle)

def draw_lobe(new_turtle, angle, side, top):
    new_turtle.forward(side)
    new_turtle.right(angle)
    new_turtle.forward(top)
    new_turtle.right(angle)
    new_turtle.forward(side)


def inward_pot_function():
	t = turtle.Turtle()

	t.shape("classic")
	t.color("red")
	t.penup()
	t.setx(-150)
	t.sety(150)
	
	number_of_lobes = int(raw_input("How many sides will your pot have? "))
	# this factor makes the template vertical vs. slanted
	angle = 360 + (360/number_of_lobes)
	side = (int(raw_input("How inches tall will each lobe be? ")))*50
	top = (int(raw_input("How inches wide will each lobe be? ")))*50

	setup_template(t, angle)

	for i in range(0,number_of_lobes):
		draw_lobe(t, angle, side, top)
		t.left(angle)

	
	saveImg()

	t.clear()




if __name__ == '__main__':
	main()