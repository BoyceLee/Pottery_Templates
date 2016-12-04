#this program will direct the user to what they want to do

from slanted_pot_template import *
from inward_angle_pot_template import *
from outward_5side_pot_template import *
from draws_fractal_to_svg import *
from draw_a_polygon import *
from draw_a_polygon_spiral import *

def menu():
    print "0 -  Main Menu"
    print "1 -  Make a pot template."
    print "2 -  Make some embellishment. I need flair!"
    print "3 -  I'm done!!!"

def menu_make_a_pot():
	print "Okay, let's make a pot. Here are the kinds of pots we can make:"
	print "1 -  I want to make a slanty pot!"
	print "2 -  I want to make pot that flairs outward."
	print "3 -  I want to make a pot that collars inward."

def menu_make_embellishment():
	print "Okay, let's make a some embellishment here. Here are the embellishments I have:"
	print "1 -  Let's have some fun with fractals."
	print "2 -  I'm more into spirals."
	print "3 -  I want some boring polygons."

def main():
	print "What do you want to do today? "
	menu()
	
	while(True):
		choice = int(raw_input("What's your choice? "))
		if choice == 0:
			menu()
		elif choice == 1:
			menu_make_a_pot()
			pot_choice = int(raw_input("Alrighty, what kind of pot are we making? "))
			if pot_choice == 1:
				slanted_pot_function()
				print "Now what do you want to do? "
				menu()
			elif pot_choice == 2:
				outward_pot_template()
				print "Now what do you want to do? "
				menu()
			elif pot_choice == 3:
				inward_pot_function()
				print "Now what do you want to do? "
				menu()
			else:
				print "Hum, are you confused? Your options are "
				menu_make_a_pot()
		elif choice == 2:
			menu_make_embellishment()
			embellishment_choice = int(raw_input("What do you want to draw on your pot? "))
			if embellishment_choice == 1:
				random_fractal()
				print "Nice fractal- now what do you want to do? "
				menu() 
			elif embellishment_choice == 2:
				draw_a_spiral()
				print "Very cool spiral! Now what do you want to do? "
				menu() 
			elif embellishment_choice == 3:
				draw_a_polygon()
				print "Now what do you want to do? "
				menu() 

		elif choice == 3:
			print "Until the next time!"
			break
		else:
			break





if __name__ == '__main__':
    main()