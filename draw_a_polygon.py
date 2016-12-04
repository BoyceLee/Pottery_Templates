from save_to_svg import saveImg
import turtle

window = turtle.Screen()
window.bgcolor("white")
turtle.screensize(canvwidth=5000, canvheight=5000, bg=None)

def draw_a_shape(new_turtle, number_of_sides, angle, length):
	new_turtle.pendown()
	new_turtle.left(angle)
	for item in range(0,number_of_sides):
		new_turtle.forward(length)
		new_turtle.left(angle)


def draw_a_polygon():
	t = turtle.Turtle()

	t.shape("classic")
	t.color("red")
	t.penup()
	t.setx(150)
	t.sety(-150)
	number_of_sides = int(raw_input("How many sides will your shape have? "))
	interior_angles = 180+((number_of_sides-3)*180)
	ea_angle = interior_angles/number_of_sides
	angle = 180 - ea_angle
	length = (int(raw_input("How many inches do you want the side of your shape? ")))*50

	draw_a_shape(t, number_of_sides, angle, length)

	saveImg()

	t.clear()

if __name__ == '__main__':
	main()