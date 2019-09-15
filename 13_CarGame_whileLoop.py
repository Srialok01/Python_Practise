"""
Problem - create a Game that takes help command from user and display below options :
start - start the car
stop - stop the car
quit - to exit the program

"""
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started !!!")
        else:
            started = True
            print(" The car is started")

    elif command == "stop":
        if not started:
            print("The car is already stopped !!!")
        else:
            started = False
            print(" The car is stopped")

    elif command == "help":
        print("""
start - start the car
stop - stop the car
quit - to exit the program
        """)
    elif command == "quit":
        print("Quiting the program !!")
        break
    elif command :
        print("didn't get you please type help for options ")
