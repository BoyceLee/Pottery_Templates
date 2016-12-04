from save_to_svg import saveImg
import turtle
window = turtle.Screen()
window.bgcolor("white")

def setup_template(new_turtle, angle_1):
	new_turtle.pendown()
	new_turtle.left(angle_1)

def draw_lobe(new_turtle, angle_1, angle_2, side, top):
	new_turtle.forward(side)
	new_turtle.right(angle_1)
	new_turtle.forward(top)
	new_turtle.right(angle_2)
	new_turtle.forward(side)




def slanted_pot_function():
	t = turtle.Turtle()

	t.shape("classic")
	t.color("red")
	t.penup()
	
	number_of_lobes = int(raw_input("How many sides will your pot have? "))
	angle_1 = (360/number_of_lobes)
	angle_2 = 180 - angle_1
	side = (int(raw_input("How inches tall will each lobe be? ")))*50
	top = (int(raw_input("How inches wide will each lobe be? ")))*50

	setup_template(t, angle_2)

	for i in range(0,number_of_lobes):
		draw_lobe(t, angle_1, angle_2, side, top)
		t.left(angle_2)

	saveImg()
	
	t.clear()
