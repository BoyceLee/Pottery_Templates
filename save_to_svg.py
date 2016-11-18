import canvasvg
import turtle

def saveImg():
    print("Done.")
    save = raw_input("Would you like to save this tree? Y/N \n")
    if save.upper() == "Y":
        turtle.hideturtle()
        name = raw_input("What would you like to name it? \n")
        nameSav = name + ".svg"
        ts = turtle.getscreen().getcanvas()
        canvasvg.saveall(nameSav, ts)
    elif save.upper() == "N":
        def runChk():
            runAgain = raw_input("Would you like to run again? Y/N (N will exit)")
            if runAgain.upper() == "Y":
                print("Running")
                main()
            elif runAgain.upper() == "N":
                print("Exiting...")
                exit()
            else:
                print("Invalid response.")
                runChk()
        runChk()
    else:
        print("Invalid response.")
        saveImg()

