from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()

drone.takeoff()
power = 20

print("Command Options: ")
print(
    "2: Circle \n"
    "3: Triangle \n"
    "4: Square \n"
    "5: Pentagon \n"
    "6: Hexagon \n"
    "w: throttle up \n"
    "s: throttle down \n"
    "a: yaw left \n"
    "d: yaw right \n"
    "i: pitch forward \n"
    "k: pitch backward \n"
    "j: roll left \n"
    "l: roll right \n"
    "q: quit")



while True:
    drone.set_throttle(0)
    drone.set_roll(0)
    drone.set_yaw(0)
    drone.set_pitch(0)

    direction = input("Input a command: ")

    if direction == "w":
        drone.set_throttle(power)

    elif direction == "s":
        drone.set_throttle(-power)

    elif direction == "a":
        drone.set_yaw(-power)

    elif direction == "d":
        drone.set_yaw(power)

    elif direction == "i":
        drone.set_pitch(power)

    elif direction == "k":
        drone.set_pitch(-power)

    elif direction == "j":
        drone.set_roll(-power)

    elif direction == "l":
        drone.set_roll(power)

    '''
    elif direction == "2":
        drone.set_roll(power)

    elif direction == "3":
        drone.set_roll(power)

    elif direction == "4":
        drone.set_roll(power)

    elif direction == "5":
        drone.set_roll(power)

    elif direction == "6":
        drone.set_roll(power)
        
    '''
    
    elif direction == "q":
        drone.land()
        break

    else:
        print("Not a command")

    drone.move(1)