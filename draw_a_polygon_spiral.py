from save_to_svg import saveImg
import turtle

window = turtle.Screen()
window.bgcolor("white")

def spiral(new_turtle, number_of_sides, angle, set_length):
	new_turtle.pendown()
	new_turtle.left(angle)
	for item in range(0,(set_length)/7):
		new_turtle.forward(set_length)
		new_turtle.left(angle)
		set_length = set_length-7


def draw_a_spiral():
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
	spiral(t, number_of_sides, angle, length)

	
	saveImg()
	
	t.clear()


if __name__ == '__main__':
	main()