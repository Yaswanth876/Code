command = ""
started = False
while True:
    command =input('>' ).lower()
    if command == "help":
        print("""start - To start the car
stop - To stop the car
quit - To exit""")
    elif command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped!")
    elif command == "quit":
        break
    else:
        print("Sorry, I can't understand that!")