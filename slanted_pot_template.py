from save_to_svg import saveImg
import turtle
window = turtle.Screen()
window.bgcolor("white")

def setup_template(new_turtle, angle_1):
	new_turtle.pendown()
	new_turtle.left(angle_1)

def draw_lobe(new_turtle, angle_1, angle_2):
    new_turtle.forward(100)
    new_turtle.right(angle_1)
    new_turtle.forward(75)
    new_turtle.right(angle_2)
    new_turtle.forward(100)



def main():
	t = turtle.Turtle()

	t.shape("classic")
	t.color("red")
	t.penup()
	
	number_of_lobes = 6
	angle_1 = (360/number_of_lobes)
	angle_2 = 180 - angle_1

	setup_template(t, angle_2)

	for i in range(0,number_of_lobes):
		draw_lobe(t, angle_1, angle_2)
		t.left(angle_2)

	# window.exitonclick()
	saveImg()



if __name__ == '__main__':
	main()